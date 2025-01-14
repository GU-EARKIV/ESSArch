/*@ngInject*/
export default ($translateProvider: ng.translate.ITranslateProvider) => {
  $translateProvider.translations('sv', {
    ACCESS: {
      ACCESS: 'Åtkomst',
      ACCESS_AID: 'Sökingång',
      ADD_ACCESS_AID: 'Lägg till sökingång',
      ADD_FIELD: 'Lägg till fält',
      ADD_FIRST_LEVEL_LOCATION: 'Lägg till placering på första nivån',
      ADD_IDENTIFIER: 'Lägg till identifikator',
      ADD_LOCATION: 'Lägg till placering',
      ADD_NODE: 'Lägg till nod',
      ADD_RELATED_ARCHIVE: 'Lägg till relaterat arkiv',
      ADD_RELATED_ARCHIVE_CREATOR: 'Lägg till relaterad arkivbildare',
      ADD_RELATION: 'Lägg till relation',
      ADD_RELATION_TO_STRUCTURE_UNIT: 'Lägg till relation till strukturenhet',
      ADD_RULE: 'Lägg till regel',
      ADD_SEARCH_AID: 'Lägg till sökingång',
      ADD_STRUCTURE_RULE: 'Lägg till ny regel för struktur',
      ADD_STRUCTURE_UNIT: 'Lägg till strukturenhet',
      ADD_TO_STRUCTURE: 'Lägg till under strukturenhet',
      ADDED_TO_TRANSFER: 'Tillagd(a) i överföring',
      ADMINISTRATIVE_DATES: 'Administrativa datum',
      AGENT_CREATE_DATE: 'Skapad',
      AGENT_REFERENCE_CODE: 'Arkivansvarigs ID',
      ALT_NAME: 'Alternativt namn',
      ALT_NAMES: 'Namn',
      APPRAISAL_DATE: 'Gallringsdatum',
      ARCHIVE: 'Arkiv',
      ARCHIVES: 'Arkiv',
      ARCHIVE_CREATOR: 'Arkivbildare',
      ARCHIVE_SAVED: 'Arkiv sparat',
      ARCHIVE_REFERENCE: 'Arkivreferens',
      ARCHIVE_RESPONSIBLE: 'Arkivansvarig',
      AUTHORIZED_NAME: 'Auktoriserat namn',
      BASIC_DATA: 'Grundläggande information',
      CAN_BE_MOVED: 'Kan flyttas',
      CAPACITY: 'Kapacitet',
      CERTAINTY: 'Visshet',
      CLASSIFICATION_STRUCTURE: 'Struktur',
      CLASSIFICATION_STRUCTURES: 'Strukturer',
      CLASSIFICATION_STRUCTURE_CREATED: 'Struktur skapad',
      CLASSIFICATION_STRUCTURE_NAME: 'Strukturs namn',
      CLASSIFICATION_STRUCTURE_REMOVED: 'Struktur borttagen',
      COMPONENT: 'Komponent',
      CONTENTS: 'Innehåll',
      CONTENT_TYPE: 'Content type',
      COULD_NOT_BE_MOVED: 'Kunde inte flyttas',
      CPF: 'Typ av auktoritetspost',
      CREATE_ACCESS_AID: 'Lägg till sökingång',
      CREATE_ARCHIVE_CREATOR: 'Skapa arkivbildare',
      CREATE_DELIVERY: 'Skapa leverans',
      CREATE_LABELS: 'Skapa etiketter',
      CREATE_NEW_FIELD: 'Skapa nytt fält',
      CREATE_NEW_STRUCTURE: 'Skapa ny struktur',
      CREATE_NEW_VERSION: 'Skapa ny version',
      CREATE_TRANSFER: 'Skapa överföring',
      CREATING: 'Skapas',
      CREATOR_NAME: 'Arkivbildarens namn',
      CREATOR_TYPE: 'Typ av arkivbildare',
      CUSTOM_FIELDS: 'Egna fält',
      COLLECTION: 'Sammling',
      DATES: 'Datum',
      DATE_MISSING: 'Datum saknas',
      DECISION_DATE: 'Beslutsdatum',
      DELETE_FIELD: 'Vill du ta bort fält: {{field}}?',
      DELIVERY: 'Leverans',
      DESELECT_FILTER: 'Ta bort filterval',
      DIP_PACKAGES: 'Utlämnandepaket',
      DOCUMENT: 'Document',
      DO_YOU_WANT_TO_REMOVE_ACCESS_AID: 'Vill du ta bort sökingång?',
      DO_YOU_WANT_TO_REMOVE_ACCESS_AID_RELATION: 'Vill du ta bort relation till sökingång?',
      DO_YOU_WANT_TO_REMOVE_AGENT_NAME: 'Vill du ta bort namn?',
      DO_YOU_WANT_TO_REMOVE_ARCHIVE_CREATOR: 'Vill du ta bort arkivbildare?',
      DO_YOU_WANT_TO_REMOVE_ARCHIVE_RELATION: 'Vill du ta bort relation till arkiv?',
      DO_YOU_WANT_TO_REMOVE_DELIVERY: 'Vill du ta bort leverans?',
      DO_YOU_WANT_TO_REMOVE_HISTORY: 'Vill du ta bort historik?',
      DO_YOU_WANT_TO_REMOVE_IDENTIFIER: 'Vill du ta bort identifikator?',
      DO_YOU_WANT_TO_REMOVE_LOCATION: 'Vill du ta bort placering?',
      DO_YOU_WANT_TO_REMOVE_MANDATE: 'Vill du ta bort grunddokument?',
      DO_YOU_WANT_TO_REMOVE_NODE: 'Vill du ta bort nod?',
      DO_YOU_WANT_TO_REMOVE_NODE_FROM_CLASSIFICATION_STRUCTURE: 'Vill du ta bort nod från struktur?',
      DO_YOU_WANT_TO_REMOVE_NOTE: 'Vill du ta bort anmärkning?',
      DO_YOU_WANT_TO_REMOVE_PLACE: 'Vill du ta bort plats?',
      DO_YOU_WANT_TO_REMOVE_RELATION: 'Vill du ta bort relation?',
      DO_YOU_WANT_TO_REMOVE_STRUCTURE: 'Vill du ta bort struktur?',
      DO_YOU_WANT_TO_REMOVE_STRUCTURE_UNIT: 'Vill du ta bort strukturenhet?',
      DO_YOU_WANT_TO_REMOVE_TRANSFER: 'Vill du ta bort överföring?',
      EDIT_ACCESS_AID: 'Redigera sökingång',
      EDIT_ARCHIVE: 'Redigera arkiv',
      EDIT_ARCHIVE_CREATOR: 'Redigera arkivbildare',
      EDIT_CLASSIFICATION_STRUCTURE: 'Redigera struktur',
      EDIT_DELIVERY: 'Editera leverans',
      EDIT_FIELD: 'Ändra fält',
      EDIT_LOCATION: 'Redigera placering',
      EDIT_RELATED_ARCHIVE: 'Redigera relation till arkiv',
      EDIT_RELATED_ARCHIVE_CREATOR: 'Redigera relation till arkivbildare',
      EDIT_RELATION_TO_STRUCTURE_UNIT: 'Redigera relation till strukturenhet',
      EDIT_SEARCH_AID: 'Redigera sökingång',
      EDIT_TRANSFER: 'Redigera leverans',
      END_DATE: 'Slutdatum',
      END_YEAR: 'Slutår',
      ERASE_SEARCH_AID: 'Vill du radera denna sökingång?',
      EXPORT_ARCHIVE: 'Utskriftsbar arkivförteckning',
      EXPORT_OPTION: 'Typ av export',
      EXPORT_OMEKA: 'Export till omeka',
      FIELD_EXISTS: 'Fältet finns redan!',
      FILE_EXTENSIONS: 'Filformat',
      FLAGGED_FOR_APPRAISAL: 'Gallras',
      FLAGGED_FOR_SECURITY: 'Sekretess',
      GO_TO_SEARCH: 'Gå till Sök',
      GLOBALSEARCHDESC_DELIVERIES: 'Lista alla leveranser som associeras med söktermen',
      GLOBALSEARCHDESC_TAGS: 'Lista alla noder som associeras med söktermen',
      GLOBALSEARCHDESC_TRANSFERS: 'Lista alla överföringar som associeras med söktermen',
      GLOBALSEARCHDESC_UNITS: 'Lista alla strukturenheter som associeras med söktermen',
      HISTORY: 'Historik',
      HITS: 'Träfflista',
      HREF: 'Länk',
      IDENTIFIER: 'Identifikator',
      IDENTIFIERS: 'Identifikatorer',
      IDS: 'IDn',
      IMPORT_DATE: 'Importdatum',
      INCLUDED_TYPES: 'Inkluderade typer',
      INCLUDE_DESCENDANT_NODES: 'Inkludera underliggande noder',
      INDEX: 'Index',
      INSTANCE: 'Instans',
      KEY: 'Nyckel',
      LANGUAGE: 'Språk',
      LATITUDE: 'Latitud',
      LEVEL: 'Nivå',
      LEVEL_OF_DETAIL: 'Detaljrikedom',
      LINK: 'Länk',
      LINK_TO_ACCESS_AID: 'Koppla sökingång',
      LINK_TO_TRANSFER: 'Lägg till i överföring',
      LINK_TO_LOCATION: 'Placera',
      LOCATION: 'Placering',
      LOCATION_FUNCTION: 'Funktion',
      LOCATION_LINK_SUCCESS: 'Placering uppdaterad',
      LONGITUDE: 'Longitud',
      MAIN: 'Efternamn',
      MAIN_CATEGORY: 'Huvudkategori',
      MANDATE: 'Grunddokument',
      MANDATES: 'Grunddokument',
      MANDATES_DESC:
        'Hänvisningar till dokument som utgör det legala grunden för tillkomsten av en institution såsom stiftelseurkund, instruktion o.dyl',
      METRIC: 'Enhet',
      METRIC_PROFILE: 'Placeringsprofil',
      NARROW_RESULTS: 'Avgränsa resultat',
      NAVIGATE_TO_TRANSFER: 'Navigera till relaterad överföring',
      NEW_ARCHIVE: 'Nytt arkiv',
      NEW_ARCHIVE_CREATED: 'Nytt arkiv skapat!',
      NEW_CLASSIFICATION_STRUCTURE: 'Ny struktur',
      NEW_FIELD: 'Nytt eget fält',
      NEW_STRUCTURE_CREATED: 'Ny struktur skapad',
      NEW_TYPE: 'Ny regel',
      NEW_VERSION: 'Ny version',
      NEW_VERSION_CREATED: 'Ny version skapad',
      NODE: 'Nod',
      NODES: 'Noder',
      NODE_ADDED: 'Tillagd!',
      NODE_EDITED: 'Uppdaterad!',
      NODE_REMOVED: 'Borttagen!',
      NODE_REMOVED_FROM_STRUCTURE: 'Nod borttagen från struktur',
      NO_ARCHIVES: 'Det finns inga arkiv ...',
      NO_CLASSIFICATION_STRUCTURES: 'Det finns inga strukturer ...',
      NO_HISTORY: 'Ingen historik tillgänglig',
      NO_REMARKS: 'Ingen anmärkning tillgänglig',
      NO_STRUCTURE_UNITS: 'Det finns inga strukturenheter ...',
      OF: 'av',
      ORGANIZATION: 'Organisation',
      PART: 'Förnamn',
      PERSONAL_IDENTIFICATION_NUMBER: 'Personnummer',
      PLACE: 'Plats',
      PLACE_IN_ARCHIVE: 'Placera i arkiv',
      PLACE_NODE_IN_ARCHIVE: 'Placera nod i arkiv',
      PLACES: 'Platser',
      PRODUCER_ORGANIZATION: 'Producent',
      PUBLISH_CLASSIFICATION_STRUCTURE: 'Publicera struktur',
      PUBLISH_CLASSIFICATION_STRUCTURE_DESC: 'Vill du publicera strukturen: {{name}}',
      PUBLISHED: 'Publicerad',
      RECORD: 'Postvisning',
      RECORD_STATUS: 'Fullständighet',
      REFERENCE_CODE: 'Referenskod',
      RELATED: 'Relaterat',
      RELATED_ACCESS_AIDS: 'Relaterade sökingångar',
      RELATED_AGENTS: 'Relaterade agenter',
      RELATED_ARCHIVE_CREATORS: 'Relaterade arkivbildare',
      RELATED_ARCHIVE_CREATORS_DESC:
        'Den arkivbildare som nämns i tabellen relaterade arkivbildare är t.ex. föregångare till den arkivbildare som visas i presentationsvyn.',
      RELATED_RESOURCES: 'Relaterade arkiv',
      RELATED_RESOURCES_DESC:
        'Den arkivbildare som visas i presentationsvyn är arkivbildare/arkivansvarig till de arkiv som visas i tabellen under ”relaterade arkiv”.',
      RELATED_STRUCTURE_UNITS: 'Relaterade strukturenheter',
      RELATIONSHIP_TYPE: 'Typ av relation',
      RELATIONSHIP_TIME_RANGE: 'Relationens tidsomfång',
      REMARKS: 'Anmärkningar',
      REMOVE_ARCHIVE: 'Ta bort arkiv',
      REMOVE_ARCHIVE_DESC: 'Vill du ta bort arkiv: {{name}}',
      REMOVE_FROM_CLASSIFICATION_STRUCTURE: 'Ta bort från struktur',
      REMOVE_LOCATION_FOR_NODE: 'Ta bort placeringslänk för: {{reference_code}} {{name}}',
      REMOVE_LOCATION_FOR_NODES: 'Ta bort placeringslänk för:',
      REMOVE_LOCATION_LINK: 'Ta bort placeringslänk',
      REMOVE_NODE: 'Ta bort',
      REMOVE_NODE_FROM_TRANSFER: 'Vill du ta bort nod: {{reference_code}} {{name}} från överföring?',
      REMOVE_NODES_FROM_TRANSFER: 'Vill du ta bort noder från överföring?',
      REMOVE_RELATION_TO_STRUCTURE_UNIT: 'Ta bort relation till strukturenhet',
      REMOVE_RELATION_TO_STRUCTURE_UNIT_DESC: 'Vill du ta bort relation till {{name}}?',
      REMOVE_SAVED_SEARCH: 'Vill du ta bort sparad sökning?',
      REMOVE_STRUCTURE_RULE: 'Ta bort regel',
      REMOVE_STRUCTURE_RULE_DESC: 'Vill du ta bort regel?',
      REMOVE_TRANSFER_LINK: 'Ta bort från överföring',
      REPLACE: 'Omplacera',
      RESOURCE_TYPE: 'Typ av arkiv',
      REVISE_DATE: 'Senast ändrad',
      RULE_ADDED: 'Regel tillagd',
      RULE_REMOVED: 'Regel borttagen',
      RULES: 'Regler',
      SAVE_RULES: 'Spara regler',
      SAVE_SEARCH: 'Spara sökning',
      SAVED_SEARCHES: 'Sparade sökningar',
      SCRIPT: 'Script',
      SECURITY_LEVEL: 'Säkerhetsnivå',
      SEE_ALL: 'Se alla',
      SEE_MORE: 'Se mer',
      SELECT_ACCESS_AID_FOR_NODE: 'Koppla {{reference_code}} {{name}} till sökingång',
      SELECT_LOCATION_FOR_NODE: 'Placera {{type.name}}: {{reference_code}} {{name}}',
      SELECT_LOCATION_FOR_NODES: 'Placera noder',
      SELECT_TRANSFER_FOR_NODE: 'Välj överföring för {{reference_code}} {{name}}',
      SELECT_TRANSFER_FOR_NODES: 'Lägg till noder i överföring',
      SEND_AS_EMAIL: 'Skicka som e-post',
      SET_CURRENT_VERSION: 'Sätt som nuvarande',
      SHOWING_RESULT: 'Visar träff',
      START_DATE: 'Startdatum',
      START_YEAR: 'Startår',
      STRUCTURE_UNIT: 'Strukturenhet',
      STRUCTURE_UNITS: 'Strukturenheter',
      SUB_CATEGORY: 'Underkategori',
      SUB_TYPE: 'Subtyp',
      SUBMITTER_ORGANIZATION: 'Avsändande organisation',
      SUBMITTER_ORGANIZATION_MAIN_ADDRESS: 'Adress',
      SUBMITTER_INDIVIDUAL: 'Kontaktperson',
      SUBMITTER_INDIVIDUAL_NAME: 'Namn',
      SUBMITTER_INDIVIDUAL_PHONE: 'Telefonnummer',
      SUBMITTER_INDIVIDUAL_EMAIL: 'E-postadress',
      SUBMITTER_INFO: 'Information om avsändare',
      SURE: 'Säker',
      TAGS_IN_LOCATION: 'Innehåll i placering',
      TAGS_IN_TRANSFER: 'Noder i överföring',
      TEMPLATE_OR_INSTANCE: 'Mall eller instans',
      TEMPLATE: 'Mall',
      TERMS_AND_CONDITION: 'Villkor',
      TEXT: 'Text',
      TIME_RANGE: 'Tidsomfång',
      TIME_RANGE_END: 'Tidsomfång slut',
      TIME_RANGE_START: 'Tidsomfång start',
      TITLE: 'Titel',
      TOPOGRAPHY: 'Topografi',
      TRANSFER: 'Överföring',
      TRANSFERS: 'Överföringar',
      UNITS_IN_TRANSFER: 'Strukturenheter i överföring',
      UNPUBLISH_CLASSIFICATION_STRUCTURE: 'Avpublicera struktur',
      UNPUBLISH_CLASSIFICATION_STRUCTURE_DESC: 'Vill du avpublicera strukturen: {{name}}',
      UNPUBLISHED: 'Avpublicerad',
      UNSURE: 'Osäker',
      UPDATE_DESCENDANTS: 'Uppdatera underliggande noder',
      USE_UUID_AS_REFCODE: 'Använd arkivets UUID som referenskod',
      VALID_DATE_END: 'Giltighetstid slut',
      VALID_DATE_START: 'Giltighetstid start',
      VERSION: 'Version',
      VERSION_HISTORY: 'Versionshistorik',
      VERSION_HISTORY_DESC: 'Lista av alla versioner av data för aktuell nod',
    },
    ARCHIVEMANAGER: 'Arkivhanterare',
    CLASSIFICATIONSTRUCTURES: 'Strukturer',
    ARCHIVECREATORS: 'Arkivbildare',
    TRANSFERS: 'Överföringar',
  });
};
