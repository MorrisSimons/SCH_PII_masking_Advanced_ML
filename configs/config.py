# PII Masking Project Configuration
PROJECT_NAME = "SCH_PII_masking_Advanced_ML"
PROJECT_VERSION = "1.0.0"

# Data Paths
DATA_RAW_PATH = "data/raw/"
DATA_PROCESSED_PATH = "data/processed/"
DATA_EXTERNAL_PATH = "data/external/"

# Model Paths
MODELS_PATH = "results/models/"
PLOTS_PATH = "results/plots/"
REPORTS_PATH = "results/reports/"

# Training Configuration
TRAIN_TEST_SPLIT = 0.9
BATCH_SIZE = 16
N_EPOCHS = 20
DROPOUT_RATE = 0.3

# Entity Types for PII Detection
PII_ENTITIES = [
    "NAME", "EMAIL", "PHONE_NUMBER", "LOCATION", 
    "CREDITCARDNUMBER", "IP", "URL", "USERNAME", 
    "JOB", "MASKEDNUMBER", "GENDER", "IBAN"
]

# AWS Configuration
AWS_REGION = "us-east-1"
AWS_COMPREHEND_ENTITIES = [
    "PERSON", "LOCATION", "ORGANIZATION", "COMMERCIAL_ITEM",
    "EVENT", "DATE", "QUANTITY", "TITLE", "OTHER"
]