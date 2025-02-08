# PII MASKER Project Notes

#### task: Mask sensetive PII data

### Original Plan

" We plan to generate synthetic data (including Swedish-specific elements such as organization numbers) to develop and test our masking solution.  We tried to find data on Kaggle with no success.

We aim to fine-tune LLM models for Swedish PII masking tasks. Especially these 3 models. 

* Deberta-v3 is one of the best models at Natural language understanding (NLU).

* DeepSeek-R1 is one of the best and largest Open Source models available to date.

* OpenAis own platform for finetuning. Compare with the most used models. "

### Problems and solutions.
- Problem: We can't use LLMs
- Solution: so we have to use NLPs
- Problem: We need a public dataset
- Solution: we use the Enron dataset.

- Problem: Missclassification with US_DRIVER_LICENSE and US_BANK_NUMBER, Handle these cases better
- Problem: Masking all the mails will take more than 350 Hours.
- Problem: Miss spellings do not get classified.
- Problem: Some names and places are still not picked up.

