import ast
import re

import pandas as pd


class dataset:
    def __init__(self, name=None, dataset=None, size=None, nlp=None, training_data=None, test_data=None):
        self.name = name if name is not None else ""
        self.size = size
        self.dataset = dataset if dataset is not None else pd.DataFrame()
        self.failed_labels = []
        self.text_accuracy = 0.0  
        self.label_accuracy = 0.0
        self.F1_score = 0.0
        self.recall = 0.0
        self.precision = 0.0
        self.NER_accuracy = 0.0
        self.token_recall = 0.0
        self.nlp = nlp
        self.training_data = training_data if training_data is not None else pd.DataFrame()
        self.test_data = test_data if test_data is not None else pd.DataFrame()

    def __repr__(self):
        return (f"dataset(name={self.name}, "
                f"size={len(self.dataset)}, "
                f"dataset={self.dataset}, "
                f"failed_labels={self.failed_labels}, "
                f"text_accuracy={self.text_accuracy:.2%}, "
                f"label_accuracy={self.label_accuracy:.2%}, "
                f"F1_score={self.F1_score:.2%}, "
                f"recall={self.recall:.2%}, "
                f"precision={self.precision:.2%}, "
                f"NER_accuracy={self.NER_accuracy:.2%}, "
                f"token_recall={self.token_recall:.2%}, "
                f"nlp={self.nlp}), "
                f"training_data={len(self.training_data)}, "
                f"test_data={len(self.test_data)}"
                )

# Solution 2 to get the unique values just to check that everything is correct with the values in template
def get_token_tokens(df):
	# Convert each token list from its string form to an actual list and get tokens != "O"
	name_tokens = {token for tokens in df["Tokens"] 
					for token in ast.literal_eval(tokens) 
					if token != "O"}
	
	# Remove the "char-" prefix from each token (if it exists)
	cleaned_name_tokens = {re.sub(r'^[A-Z]-', '', token) for token in name_tokens}
	return cleaned_name_tokens, name_tokens

# Solution 1 to get the unique values just to check that everything is correct with the values in tokens
def get_template_tokens(df):
    # Use df_ground_truth as the dataset for ground truth
    # Regex to extract values inside square brackets from each row in df_ground_truth
    unique_matches = set()
    for text in df["Template"].dropna():
        matches = re.findall(r'\[([^]]+)\]', text)
        unique_matches.update(matches)

   

    # Clean the unique_matches set by removing the trailing underscore and everything
    cleaned_matches = {re.sub(r'_[^_]+$', '', token) for token in unique_matches}
    return cleaned_matches, unique_matches

def count_labeled_items(df):
	"""
	Counts the total number of labeled items in the 'Template' column of a DataFrame.
	"""
	total_count = 0
	for text in df['Template']:
		# Find all occurrences of labels enclosed in square brackets
		labels = re.findall(r'\[.*?\]', text)
		total_count += len(labels)
	return total_count