# AI-Project

Python version : 3.8.10 

Use of the following libraries in this project :

- For the similarity score between two documents : https://github.com/Coding-bot007/Semantic-text-similarity
- For the prediction of EuroVoc descriptors : https://github.com/racai-ai/pyeurovoc
------------------------------------------------------------------------------------------------------------------
Similarity_score.py

The goal with the similarity_score.py is to measure the semantic text similarity between two sentences :
- it measure the meaning of the sentence but also the semantic word by word.

In this file, the code is comparing two sentences :
- AI point which is the statement from AI Act you want to compare with all statements from the GDPR Article.
As it is comparing with a lot of statements, it might take a while (15-20 minutes).
-------------------------------------------------------------------------------------------------------------------
EuroVoc_2.xlsx is the Excel file which contain all statements from AI Act and GDPR Article and their predicted descriptors.

EuroVoc_copie_3.xlsx is the Excel file which contain all highest similarity scores for each statement from the AI Act (compared with each statement from GDPR Article).

eurovoc_export_en_modif.xlsx is the Excel file with EuroVoc descriptors and their ID.

Available here : 
- https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/eurovoc



