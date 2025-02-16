# Data Preprocessing & Entity Masking

This document outlines how to preprocess text data and manage entity categories (e.g., **NAME**, **LOCATION**, **GENDER**). It also covers which entities to remove entirely, how to handle normalization, and the overall evaluation steps.

---

## 1. Entity Standardization

### 1.1 Name Entities
- **Original Labels**: `NAME_1`, `NAME_N`, etc.  
- **Mapped To**: `NAME`  

### 1.2 Merging Entity Types
Below is a mapping of multiple related entity labels into a single label:

- **LOCATION**  
  - Includes: `STREETADDRESS`, `SECONDARYADDRESS`, `BUILDINGNUMBER`, `STREET`, `CITY`, `STATE`, `COUNTY`, `NEARBYGPSCOORDINATE`, `ZIPCODE`
- **GENDER**  
  - Includes: `SEXTYPE`, `SEX`
- **NAME**  
  - Includes: `FULLNAME`, `FIRSTNAME`, `LASTNAME`
- **IP**  
  - Includes: `IPV4`, `IP`, `IPV6`, `MAC`
- **JOB**  
  - Includes: `JOBDESCRIPTOR`, `JOBTYPE`, `JOBTITLE`, `JOBAREA`
- **MASKED_NUMBER**  
  - Includes: `NUMBER`, `MASKED_NUMBER`, `AMOUNT`, `ACCOUNTNUMBER`, `CREDITCARDCVV`, `PIN`, `BUILDINGNUMBER`

### 1.3 Entities to Remove
These entity labels should be **discarded** entirely from the dataset:
- `ORDINALDIRECTION`
- `ACCOUNTNAME`
- `CURRENCYSYMBOL`
- `CURRENCYNAME`
- `CURRENCY`
- `CURRENCYCODE`
- `CREDITCARDISSUER`
- `ETHEREUMADDRESS`
- `LITECOINADDRESS`
- `BITCOINADDRESS`

---

## 2. Preprocessing Steps

1. **Scale Down / Mask Entities**  
   - *(Completed)* ~~Reduce the variety of entity labels by merging them into broader categories. Then mask them in the text as needed.~~

2. **Data Preparation**  
   - *(Completed)* ~~Normalization, stemming or lemmatization, and tokenization.~~  

3. **Research Sentence Splitting**  
   - *(Completed)* ~~Evaluate approaches to segment text into sentences (e.g., using spaCy or regex).~~

4. **Build model**
 
---

## 3. Evaluation

1. **Evaluate the Model**  
   - Train and test your model on the processed dataset.  
2. **Apply Regex**  
   - *(Planned)* Use regular expressions for additional filtering or masking. Then test and evaluate how this impacts model performance.
3. **Test diffrent things**
---

## 4. Additional Tasks

1. **Data Visualization**  
   - Language detection or other exploratory data analysis.
2. **Amazon Comprehend**  
   - Consider integrating or comparing results with Amazon Comprehend for entity detection, sentiment analysis, or other NLP features.
3. **Write an report**
---

### Summary

- **Entity Mapping**: Merge and rename entity labels to simplify your dataset.  
- **Entity Removal**: Drop entities that aren’t needed.  
- **Text Preprocessing**: Normalize text, optionally perform stemming or lemmatization, then tokenize.  
- **Sentence Splitting**: Use a reliable library (e.g., spaCy) if your workflow benefits from per-sentence analysis.  
- **Model & Regex Evaluation**: Train your model and refine with regex-based post-processing if needed.  

