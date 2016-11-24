"""
    ESSArch Tools - ESSArch is an Electronic Preservation Platform
    Copyright (C) 2005-2016  ES Solutions AB

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Contact information:
    Web - http://www.essolutions.se
    Email - essarch@essolutions.se
"""

# Create your models here.
from __future__ import division

from _version import get_versions

from celery import states as celery_states

from collections import OrderedDict

from django.conf import settings
from django.db import models

from ESSArch_Core.configuration.models import (
    EventType, Path,
)

from ESSArch_Core.WorkflowEngine.models import (
    ProcessStep, ProcessTask,
)

from ESSArch_Core.profiles.models import (
    SubmissionAgreement as SA,
    ProfileIP, ProfileSA,
)

from ESSArch_Core.util import (
    create_event,
    creation_date,
    get_tree_size_and_count,
    timestamp_to_datetime,
)

from ESSArch_Core.essxml.Generator.xmlGenerator import (
    downloadSchemas, find_destination
)

from scandir import scandir, walk

import hashlib, json, math, os, uuid


class ArchivalInstitution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'ArchivalInstitution'

    def __unicode__(self):
        # create a unicode representation of this object
        return '%s - %s' % (self.name, self.id)


class ArchivistOrganization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'ArchivistOrganization'

    def __unicode__(self):
        # create a unicode representation of this object
        return '%s - %s' % (self.name, self.id)


class ArchivalType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'ArchivalType'

    def __unicode__(self):
        # create a unicode representation of this object
        return '%s - %s' % (self.name, self.id)


class ArchivalLocation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'ArchivalLocation'

    def __unicode__(self):
        # create a unicode representation of this object
        return '%s - %s' % (self.name, self.id)


class InformationPackage(models.Model):
    """
    Informaion Package
    """

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    ObjectIdentifierValue = models.CharField(max_length=255, null=True)
    Label = models.CharField(max_length=255)
    Content = models.CharField(max_length=255)
    Responsible = models.CharField(max_length=255)
    CreateDate = models.DateTimeField(auto_now_add=True)
    State = models.CharField(max_length=255)
    ObjectPath = models.CharField(max_length=255)
    Startdate = models.DateTimeField(null=True)
    Enddate = models.DateTimeField(null=True)
    OAIStype = models.CharField(max_length=255)
    SubmissionAgreement = models.ForeignKey(
        SA,
        on_delete=models.CASCADE,
        related_name='information_packages',
        default=None,
        null=True,
    )
    SubmissionAgreementLocked = models.BooleanField(default=False)
    ArchivalInstitution = models.ForeignKey(
        ArchivalInstitution,
        on_delete=models.CASCADE,
        related_name='information_packages',
        default=None,
        null=True
    )
    ArchivistOrganization = models.ForeignKey(
        ArchivistOrganization,
        on_delete=models.CASCADE,
        related_name='information_packages',
        default=None,
        null=True
    )
    ArchivalType = models.ForeignKey(
        ArchivalType,
        on_delete=models.CASCADE,
        related_name='information_packages',
        default=None,
        null=True
    )
    ArchivalLocation = models.ForeignKey(
        ArchivalLocation,
        on_delete=models.CASCADE,
        related_name='information_packages',
        default=None,
        null=True
    )

    def save(self, *args, **kwargs):
        super(InformationPackage, self).save(*args, **kwargs)

        if not self.ObjectIdentifierValue:
            self.ObjectIdentifierValue = str(self.pk)
            self.save()

    @property
    def ObjectSizeAndNum(self):
        return get_tree_size_and_count(self.ObjectPath)

    def get_profile_rel(self, profile_type):
        return self.profileip_set.filter(
            profile__profile_type=profile_type
        ).first()

    def profile_locked(self, profile_type):
        rel = self.get_profile_rel(profile_type)

        if rel:
            return rel.LockedBy is not None

        return False

    def get_profile(self, profile_type):
        rel = self.get_profile_rel(profile_type)

        if rel:
            return rel.profile

        return None

    def change_profile(self, new_profile):
        ptype = new_profile.profile_type
        try:
            pip = ProfileIP.objects.get(ip=self, profile__profile_type=ptype)
            pip.profile = new_profile
            pip.save()
        except ProfileIP.DoesNotExist:
            ProfileIP.objects.create(ip=self, profile=new_profile)

    def unlock_profile(self, ptype):
        ProfileIP.objects.filter(
            ip=self, profile__profile_type=ptype
        ).delete()

    def get_container_format(self):
        try:
            return self.get_profile('transfer_project').specification_data.get(
                'container_format', 'tar'
            )
        except:
            return 'tar'

    def get_checksum_algorithm(self):
        try:
            name = self.get_profile('transfer_project').specification_data.get(
                'checksum_algorithm', 'sha256'
            )
        except:
            name = 'sha256'

        return name

    def create(self, validate_logical_physical_representation=True,
               validate_xml_file=True, validate_file_format=True,
               validate_integrity=True):

        container_format = self.get_container_format()

        t0 = ProcessTask.objects.create(
            name="preingest.tasks.UpdateIPStatus",
            params={
                "ip": self,
                "status": "Creating",
            },
            processstep_pos=0,
            information_package=self
        )
        start_create_sip_step = ProcessStep.objects.create(
            name="Update IP Status",
            parent_step_pos=0
        )

        start_create_sip_step.tasks.add(t0)

        event_type = EventType.objects.get(eventType=10200)

        create_event(event_type, 0, "Created SIP", get_versions()['version'], "System", ip=self)

        prepare_path = Path.objects.get(
            entity="path_preingest_prepare"
        ).value

        reception_path = Path.objects.get(
            entity="path_preingest_reception"
        ).value

        ip_prepare_path = os.path.join(prepare_path, str(self.pk))
        ip_reception_path = os.path.join(reception_path, str(self.pk))
        events_path = os.path.join(ip_prepare_path, "ipevents.xml")

        structure = self.get_profile('sip').structure

        info = self.get_profile('sip').specification_data
        info["_OBJID"] = str(self.pk)
        info["_OBJLABEL"] = self.Label

        # ensure premis is created before mets
        filesToCreate = OrderedDict()

        if self.profile_locked('preservation_metadata'):
            premis_profile = self.get_profile('preservation_metadata')
            premis_dir, premis_name = find_destination("preservation_description_file", structure)
            premis_path = os.path.join(self.ObjectPath, premis_dir, premis_name)
            filesToCreate[premis_path] = premis_profile.specification

        mets_dir, mets_name = find_destination("mets_file", structure)
        mets_path = os.path.join(self.ObjectPath, mets_dir, mets_name)
        filesToCreate[mets_path] = self.get_profile('sip').specification

        for fname, template in filesToCreate.iteritems():
            dirname = os.path.dirname(fname)
            downloadSchemas(
                template, dirname, structure=structure, root=self.ObjectPath
            )

        t1 = ProcessTask.objects.create(
            name="preingest.tasks.GenerateXML",
            params={
                "info": info,
                "filesToCreate": filesToCreate,
                "folderToParse": ip_prepare_path,
                "algorithm": self.get_checksum_algorithm(),
            },
            processstep_pos=3,
            information_package=self
        )

        generate_xml_step = ProcessStep.objects.create(
            name="Generate XML",
            parent_step_pos=1
        )
        generate_xml_step.tasks = [t1]
        generate_xml_step.save()

        #dirname = os.path.join(ip_prepare_path, "data")

        validate_step = ProcessStep.objects.create(
            name="Validation",
            parent_step_pos=2
        )

        if validate_xml_file:
            validate_step.tasks.add(
                ProcessTask.objects.create(
                    name="preingest.tasks.ValidateXMLFile",
                    params={
                        "xml_filename": mets_path,
                    },
                    processstep_pos=1,
                    information_package=self
                )
            )

            if self.profile_locked("preservation_metadata"):
                validate_step.tasks.add(
                    ProcessTask.objects.create(
                        name="preingest.tasks.ValidateXMLFile",
                        params={
                            "xml_filename": premis_path,
                        },
                        processstep_pos=2,
                        information_package=self
                    )
                )

        if validate_logical_physical_representation:
            validate_step.tasks.add(
                ProcessTask.objects.create(
                    name="preingest.tasks.ValidateLogicalPhysicalRepresentation",
                    params={
                        "xmlfile": mets_path,
                        "ip": self
                    },
                    processstep_pos=3,
                    information_package=self
                )
            )

        validate_step.tasks.add(
            ProcessTask.objects.create(
                name="ESSArch_Core.tasks.ValidateFiles",
                params={
                    "ip": self,
                    "xmlfile": mets_path,
                    "validate_fileformat": validate_file_format,
                    "validate_integrity": validate_integrity,
                },
                processstep_pos=4,
                information_package=self
            )
        )

        validate_step.save()

        info = self.get_profile('event').specification_data
        info["_OBJID"] = str(self.pk)
        info["_OBJLABEL"] = self.Label

        filesToCreate = OrderedDict()
        filesToCreate[events_path] = self.get_profile('event').specification

        for fname, template in filesToCreate.iteritems():
            dirname = os.path.dirname(fname)
            downloadSchemas(
                template, dirname, structure=structure, root=self.ObjectPath
            )

        create_sip_step = ProcessStep.objects.create(
                name="Create SIP",
                parent_step_pos=3
        )

        create_sip_step.tasks.add(ProcessTask.objects.create(
            name="preingest.tasks.GenerateXML",
            params={
                "info": info,
                "filesToCreate": filesToCreate,
                "algorithm": self.get_checksum_algorithm(),
            },
            processstep_pos=0,
            information_package=self
        ))

        create_sip_step.tasks.add(ProcessTask.objects.create(
            name="preingest.tasks.AppendEvents",
            params={
                "filename": events_path,
            },
            processstep_pos=1,
            information_package=self
        ))

        spec = {
            "-name": "object",
            "-namespace": "premis",
            "-children": [
                {
                    "-name": "objectIdentifier",
                    "-namespace": "premis",
                    "-children": [
                        {
                            "-name": "objectIdentifierType",
                            "-namespace": "premis",
                            "#content": [{"var": "FIDType"}],
                            "-children": []
                        },
                        {
                            "-name": "objectIdentifierValue",
                            "-namespace": "premis",
                            "#content": [{"var": "FID"}],
                            "-children": []
                        }
                    ]
                },
                {
                    "-name": "objectCharacteristics",
                    "-namespace": "premis",
                    "-children": [
                        {
                            "-name": "format",
                            "-namespace": "premis",
                            "-children": [
                                {
                                    "-name": "formatDesignation",
                                    "-namespace": "premis",
                                    "-children": [
                                        {
                                            "-name": "formatName",
                                            "-namespace": "premis",
                                            "#content": [{"var": "FFormatName"}],
                                            "-children": []
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "-name": "storage",
                    "-namespace": "premis",
                    "-children": [
                        {
                            "-name": "contentLocation",
                            "-namespace": "premis",
                            "-children": [
                                {
                                    "-name": "contentLocationType",
                                    "-namespace": "premis",
                                    "#content": [{"var": "FLocationType"}],
                                    "-children": []
                                },
                                {
                                    "-name": "contentLocationValue",
                                    "-namespace": "premis",
                                    "#content": [{"text": "file:///%s.%s" % (self.pk, container_format.lower())}],
                                    "-children": []
                                }
                            ]
                        }
                    ]
                }
            ],
            "-attr": [
                {
                  "-name": "type",
                  '-namespace': 'xsi',
                  "-req": "1",
                  "#content": [{"text":"premis:file"}]
                }
            ],
        }

        info = {
            'FIDType': "UUID",
            'FID': self.ObjectIdentifierValue,
            'FFormatName': container_format.upper(),
            'FLocationType': 'URI',
            'FName': self.ObjectPath,
        }

        create_sip_step.tasks.add(ProcessTask.objects.create(
            name="ESSArch_Core.tasks.InsertXML",
            params={
                "filename": events_path,
                "elementToAppendTo": "premis",
                "spec": spec,
                "info": info,
                "index": 0
            },
            processstep_pos=2,
            information_package=self
        ))

        if validate_xml_file:
            create_sip_step.tasks.add(
                ProcessTask.objects.create(
                    name="preingest.tasks.ValidateXMLFile",
                    params={
                        "xml_filename": events_path,
                    },
                    processstep_pos=3,
                    information_package=self
                )
            )


        if container_format.lower() == 'zip':
            zipname = os.path.join(ip_reception_path) + '.zip'
            create_sip_step.tasks.add(
                ProcessTask.objects.create(
                    name="preingest.tasks.CreateZIP",
                    params={
                        "dirname": ip_prepare_path,
                        "zipname": zipname,
                    },
                    processstep_pos=4,
                    information_package=self
                )
            )

        else:
            tarname = os.path.join(ip_reception_path) + '.tar'
            create_sip_step.tasks.add(
                ProcessTask.objects.create(
                    name="preingest.tasks.CreateTAR",
                    params={
                        "dirname": ip_prepare_path,
                        "tarname": tarname,
                    },
                    processstep_pos=5,
                    information_package=self
                )
            )

        create_sip_step.tasks.add(
            ProcessTask.objects.create(
                name="preingest.tasks.UpdateIPStatus",
                params={
                    "ip": self,
                    "status": "Created",
                },
                processstep_pos=6,
                information_package=self
            )
        )

        create_sip_step.save()

        main_step = ProcessStep.objects.create(
            name="Create SIP",
        )
        main_step.child_steps = [
            start_create_sip_step, generate_xml_step, validate_step,
            create_sip_step
        ]
        main_step.information_package = self
        main_step.save()
        main_step.run()

    def submit(self):
        step = ProcessStep.objects.create(
            name="Submit SIP",
            information_package = self
        )

        step.tasks.add(ProcessTask.objects.create(
            name="preingest.tasks.UpdateIPStatus",
            params={
                "ip": self,
                "status": "Submitting",
            },
            processstep_pos=0,
            information_package=self
        ))

        reception = Path.objects.get(entity="path_preingest_reception").value

        sd_profile = self.get_profile('submit_description')

        container_format = self.get_container_format()
        container_file = os.path.join(reception, str(self.pk) + ".%s" % container_format.lower())

        sa = self.SubmissionAgreement

        info = sd_profile.specification_data
        info["_OBJID"] = str(self.pk)
        info["_OBJLABEL"] = str(self.Label)
        info["_IP_CREATEDATE"] = timestamp_to_datetime(creation_date(container_file)).isoformat()
        info["_SA_ID"] = str(sa.pk)

        try:
            info["_PROFILE_TRANSFER_PROJECT_ID"] = str(self.get_profile('transfer_project').pk)
        except AttributeError:
            pass

        try:
            info["_PROFILE_SUBMIT_DESCRIPTION_ID"] = str(self.get_profile('submit_description').pk)
        except AttributeError:
            pass

        try:
            info["_PROFILE_SIP_ID"] = str(self.get_profile('sip').pk)
        except AttributeError:
            pass

        try:
            info["_PROFILE_AIP_ID"] = str(self.get_profile('aip').pk)
        except AttributeError:
            pass

        try:
            info["_PROFILE_DIP_ID"] = str(self.get_profile('dip').pk)
        except AttributeError:
            pass

        try:
            info["_PROFILE_CONTENT_TYPE_ID"] = str(self.get_profile('content_type').pk)
        except AttributeError:
            pass

        try:
            info["_PROFILE_AUTHORITY_INFORMATION_ID"] = str(self.get_profile('authority_information').pk)
        except AttributeError:
            pass

        try:
            info["_PROFILE_ARCHIVAL_DESCRIPTION_ID"] = str(self.get_profile('archival_description').pk)
        except AttributeError:
            pass

        try:
            info["_PROFILE_PRESERVATION_METADATA_ID"] = str(self.get_profile('preservation_metadata').pk)
        except AttributeError:
            pass

        try:
            info["_PROFILE_EVENT_ID"] = str(self.get_profile('event').pk)
        except AttributeError:
            pass

        try:
            info["_PROFILE_DATA_SELECTION_ID"] = str(self.get_profile('data_selection').pk)
        except AttributeError:
            pass

        try:
            info["_PROFILE_IMPORT_ID"] = str(self.get_profile('import').pk)
        except AttributeError:
            pass

        try:
            info["_PROFILE_WORKFLOW_ID"] = str(self.get_profile('workflow').pk)
        except AttributeError:
            pass


        infoxml = os.path.join(reception, str(self.pk) + ".xml")

        filesToCreate = {
            infoxml: sd_profile.specification
        }

        step.tasks.add(ProcessTask.objects.create(
            name="preingest.tasks.GenerateXML",
            params={
                "info": info,
                "filesToCreate": filesToCreate,
                "folderToParse": container_file,
                "algorithm": self.get_checksum_algorithm(),
            },
            processstep_pos=1,
            information_package=self
        ))

        step.tasks.add(ProcessTask.objects.create(
            name="preingest.tasks.SubmitSIP",
            params={
                "ip": self
            },
            processstep_pos=2,
            information_package=self
        ))

        step.tasks.add(ProcessTask.objects.create(
            name="preingest.tasks.UpdateIPStatus",
            params={
                "ip": self,
                "status": "Submitted"
            },
            processstep_pos=3,
            information_package=self
        ))

        step.save()
        step.run()

    @property
    def step_state(self):
        """
        Gets the state of the IP based on its steps

        Args:

        Returns:
            Can be one of the following:
            SUCCESS, STARTED, FAILURE, PENDING

            Which is decided by five scenarios:

            * If there are no steps, then PENDING.
            * If there are steps and they are all pending,
              then PENDING.
            * If a step has started, then STARTED.
            * If a step has failed, then FAILURE.
            * If all steps have succeeded, then SUCCESS.
        """

        steps = self.steps.all()
        state = celery_states.SUCCESS

        if not steps:
            return celery_states.PENDING

        for step in steps:
            step_status = step.status

            if step_status == celery_states.STARTED:
                state = step_status
            if (step_status == celery_states.PENDING and
                    state != celery_states.STARTED):
                state = step_status
            if step_status == celery_states.FAILURE:
                return step_status

        return state

    def status(self):
        if self.State in ["Prepared", "Created", "Submitted"]:
            return 100

        if self.State == "Preparing":
            if self.SubmissionAgreementLocked:
                return 100

            progress = 33

            try:
                sa_profiles = ProfileSA.objects.filter(
                    submission_agreement=self.SubmissionAgreement
                )

                ip_profiles_locked = ProfileIP.objects.filter(
                    ip=self, LockedBy__isnull=False,
                    profile__profile_type__in=sa_profiles.values(
                        "profile__profile_type"
                    )
                )

                progress += math.ceil(ip_profiles_locked.count() * (33 / sa_profiles.count()))

            except ZeroDivisionError:
                pass

            return progress

        if self.State in ["Creating", "Submitting", "Receiving"]:
            steps = self.steps.all()

            if steps:
                try:
                    progress = sum([s.progress() for s in steps])
                    return progress / len(steps)
                except:
                    return 0

            return 0

    def delete(self, *args, **kwargs):
        super(InformationPackage, self).delete(*args, **kwargs)
        ArchivalInstitution.objects.filter(
            information_packages__isnull=True
        ).delete()
        ArchivistOrganization.objects.filter(
            information_packages__isnull=True
        ).delete()
        ArchivalType.objects.filter(
            information_packages__isnull=True
        ).delete()
        ArchivalLocation.objects.filter(
            information_packages__isnull=True
        ).delete()

    class Meta:
        ordering = ["id"]
        verbose_name = 'Information Package'

    def __unicode__(self):
        # create a unicode representation of this object
        return '%s - %s' % (self.Label, self.pk)

    def get_value_array(self):
        # make an associative array of all fields  mapping the field
        # name to the current value of the field
        return {
            field.name: field.value_to_string(self)
            for field in InformationPackage._meta.fields
        }


class EventIP(models.Model):
    """
    Events related to IP
    """

    OUTCOME_CHOICES = (
        (0, 'Success'),
        (1, 'Fail')
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    eventType = models.ForeignKey(
        'configuration.EventType',
        on_delete=models.CASCADE
    )
    eventDateTime = models.DateTimeField(auto_now_add=True)
    eventApplication = models.ForeignKey(
        'WorkflowEngine.ProcessTask', on_delete=models.CASCADE, null=True
    ) # The task that generated the event
    eventVersion = models.CharField(max_length=255) # The version number of the application (from versioneer)
    eventOutcome = models.IntegerField(choices=OUTCOME_CHOICES, null=True, default=None) # Success (0) or Fail (1)
    eventOutcomeDetailNote = models.CharField(max_length=1024) # Result or traceback from IP
    linkingAgentIdentifierValue = models.CharField(max_length=255)
    linkingObjectIdentifierValue = models.ForeignKey(
        'InformationPackage',
        on_delete=models.CASCADE,
        related_name='events'
    )

    def getEventOutcomeDetailNote(self):
        max_len = 1024
        task = self.eventApplication

        if task and task.status == celery_states.FAILURE:
            prefix = "%s (%s) failed: " % (task.name, task.pk)
            exception = task.exception

            total_len = len(prefix) + len(exception)

            if total_len > max_len:
                suffix = ' (truncated)'
                return (prefix + exception)[:max_len - len(suffix)] + suffix

            return prefix + exception

        return self.eventOutcomeDetailNote

    class Meta:
        ordering = ["eventType"]
        verbose_name = 'Events related to IP'

    def __unicode__(self):
        # create a unicode representation of this object
        return '%s (%s)' % (self.eventType.eventDetail, self.id)

    def get_value_array(self):
        # make an associative array of all fields  mapping the field
        # name to the current value of the field
        return {
            field.name: field.value_to_string(self)
            for field in EventIP._meta.fields
        }