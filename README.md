# AI-Project

Modif à faire :
--
Décrire les fichiers Excel, ajouter les nouveaux fichiers python. Mettre le text_extraction.py ?
Description globale du repository.

Python version : 3.8.10 

----------------
similarity_score.py
------------------------------------------------------------------------------------------------------------------

The library semantic-text-similarity was used for this file : https://github.com/Coding-bot007/Semantic-text-similarity

The goal with the similarity_score.py is to measure the semantic text similarity between two sentences :
- it measure the meaning of the sentence but also the semantic word by word.

In this file, the code is comparing two sentences :
- AI point which is the statement from AI Act you want to compare with all statements from the GDPR Article.
As it is comparing with a lot of statements, it might take a while (15-20 minutes).

There is also a condition which will keep the highest similarity score and add in the similary_whole_ai.xlsx if the current similarity score is higher than the old one.

-----------
descriptors_prediction.py
-------------------------------------------------------------------------------------------------------------------

The library pyeurovoc was used for this file : https://github.com/racai-ai/pyeurovoc

This file predict the labels for each statements in the Excel file.
The prediction gives labels associated with probability [0:1] which means :
- 0 is complete dissimilarity
- 1 is complete similarity

You can also select how many labels you want, it usually give 6 labels but you can choose with the num_labels parameter.

This code is also taking all the labels to put them into a list, to remove the percentage from the predicted labels. I made a conversion from string to int for the labels.

-------------------------------
descriptors_conversion.py
----------------------------------------

This file use the output you have with descriptors_prediction.py and also the Excel file available here : 
- https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/eurovoc

This code is doing a dictionary of ID descriptors and EuroVoc descriptors to put the EuroVoc descriptors along the labels.

-------------------------------------------

EuroVoc_2.xlsx is the Excel file which contain all statements from AI Act and GDPR Article and their predicted descriptors.

EuroVoc_copie_3.xlsx is the Excel file which contain all highest similarity scores for each statement from the AI Act (compared with each statement from GDPR Article).

eurovoc_export_en_modif.xlsx is the Excel file with EuroVoc descriptors and their ID (convert into int type).




