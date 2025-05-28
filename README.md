# PII Masking Tool with Amazon comprehend Performance
A comprehensive machine learning project for detecting and masking Personally Identifiable Information (PII) in text data, achieving performance comparable to Amazon Comprehend.

![top language](https://img.shields.io/github/languages/top/gpt-null/template)
![code size](https://img.shields.io/github/languages/code-size/gpt-null/template)
![last commit](https://img.shields.io/github/last-commit/gpt-null/template)
![issues](https://img.shields.io/github/issues/gpt-null/template)
![contributors](https://img.shields.io/github/contributors/gpt-null/template)
![License](https://img.shields.io/github/license/gpt-null/template)

## Performance Comparison

Per-entity precision (P), recall (R), and F1-score of the custom model vs. Amazon Comprehend on the test set. The overall row indicates macro-averaged scores across all entity types.

| Entity | Custom Model | | | Amazon Comprehend | | |
|--------|-------------|---|---|-------------------|---|---|
| | P | R | F1 | P | R | F1 |
| Name | 99.8% | 99.9% | 99.9% | 100.0% | 99.8% | 99.9% |
| UserAgent | 90.9% | 90.9% | 90.9% | 92.3% | 92.3% | 92.3% |
| Password | 60.0% | 54.5% | 57.1% | 93.3% | 100.0% | 96.6% |
| Username | 98.0% | 98.0% | 98.0% | 100.0% | 97.1% | 98.6% |
| URL | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| CreditCardNumber | 45.0% | 45.0% | 45.0% | 81.8% | 100.0% | 90.0% |
| IP | 90.4% | 98.7% | 94.3% | 96.3% | 94.5% | 95.4% |
| Gender | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% | 100.0% |
| Location | 96.8% | 96.9% | 96.9% | 97.5% | 95.7% | 96.6% |
| Job | 99.7% | 99.7% | 99.7% | 99.7% | 100.0% | 99.9% |
| Email | 100.0% | 100.0% | 100.0% | 99.9% | 100.0% | 100.0% |
| IBAN | 50.0% | 33.3% | 40.0% | 100.0% | 100.0% | 100.0% |
| MaskedNumber | 93.8% | 95.5% | 94.6% | 95.8% | 95.8% | 95.8% |
| **Overall** | **98.9%** | **99.1%** | **99.0%** | **99.2%** | **98.7%** | **99.0%** |


