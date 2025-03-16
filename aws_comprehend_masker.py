import os

import boto3
import pandas as pd
from dotenv import load_dotenv
from tqdm import tqdm

# Load environment variables and AWS credentials
load_dotenv()
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

# Initialize the AWS Comprehend client
client = boto3.client(
	'comprehend',
	region_name='us-east-1',
	aws_access_key_id=aws_access_key_id,
	aws_secret_access_key=aws_secret_access_key
)

# Custom entity recognizer endpoint
custom_endpoint_arn = "arn:aws:comprehend:us-east-1:225989367081:entity-recognizer-endpoint/MODEL1Test"

def mask_text(text, entities):
	"""Mask entities in text with [MASKED] placeholder"""
	masked_text = text
	# Process entities in reverse order to avoid offset issues
	for entity in sorted(entities, key=lambda x: x['BeginOffset'], reverse=True):
		start = entity['BeginOffset']
		end = entity['EndOffset']
		masked_entity = entity['Type']
		masked_text = masked_text[:start] + f"[ {masked_entity} ]" + masked_text[end:]
	return masked_text

def process_text(text):
	"""Get entities from AWS Comprehend and mask them"""
	response = client.detect_entities(
		Text=text,
		LanguageCode='en',
		EndpointArn=custom_endpoint_arn
	)
	return mask_text(text, response.get('Entities', []))

# Load data
print("Loading data...")
df = pd.read_csv('./aws_testing_data.csv')
text_column = df.columns[0]

# Process rows
print("Masking PII data...")
df['masked_text'] = None
for i, row in tqdm(df.iterrows(), total=len(df)):
	df.at[i, 'masked_text'] = process_text(row[text_column])
	
	# Save one more time after 200 lines
	if i + 1 == 50:
		print(f"Saving second checkpoint at row {i+1}...")
		df.to_csv(f'./masked_data_checkpoint_{i+1}.csv', index=False)

# Save results
print("Saving results...")
df.to_csv('./masked_data.csv', index=False)
print("Done!")
