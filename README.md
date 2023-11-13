# AI-Project

The goal of this project is to find the gaps between AI Act and other standards which are related to data sharing in Health Data Spaces in EU.
Using AI Act and GDPR, we will use ChatGPT to find these gaps.
We will then create a RDF file to visualize a knowledge graph.

Python version : 3.8.10 

----------------
ai_act_extracter.py & gdpr_extracter.py
------------------------------------------------------------------------------------------------------------------

This file is used to extract all statements from AI Act based on a HTML file modified.
Either you have to modify the AI Act HTML file with good tags for class, or you have to modify the python code to use it on your own HTML file.

The second file is used to do the same thing but with the GDPR HTML file.

competency_questions_evaluated.py
-------------------------------------------------------------------------------------------------------------------

This Python file is used to determine competency questions from GDPR statements using ChatGPT API.
The aim is to find the gaps between GDPR and AI Act.

questions_gdpr_filter.py
----------------------------------------

This file is used to filter competency questions, which means that if these questions are related to data sharing or not.
Once we have all questions related to data sharing, we can proceed further with the next Python file.

questions_label_generation.py
----------------------------------------

This file is used to generate labels of 3-4 words based on the competency questions that are related to data sharing.
These labels will be used to make groups of questions.

aiact_descripency.py
----------------------------------------

After generating these labels, you have to know if these questions are mentionned in the AI ACT.
With this file, you can query ChatGPT with your own database.
The database for us will be the AI ACT.
You can then query ChatGPT to ask if these competency questions are mentionned in the AI ACT.
We will keep all "NO" answers from these results.

excel_to_rdf.py
----------------------------------------

Once you have done all the previous steps, you can now create your RDF file which will be used for the knowledge graph.
With this file, you will generate a RDF file in Turtle format using data you have stocked in the Excel file.
This will create the node Concept with the labels and then other nodes called "Questions" that will be related to Concept nodes.
In "Questions" nodes, you will have the definition which is the original statement from GDPR (the question is based on this statement) and then you will have the explanation which is the explanation of the gap between GDPR and AI Act on this question.

knowledge_graph.py
----------------------------------------

Now that you have the RDF file, you can now create the knowledge graph with the use of Kglab's python library, which allow you to visualize your graph on a web interface.
You can also use other applications to visualize your graph.

-------------------------------------------
Excel files
-------------------------------------------
ai_act_statements.xlsx is the Excel which contain all the statements from the Artificial Intelligence Act (HTML file) from Article 1 to Article 85.

gdpr_statements.xlsx is the Excel file which contain all statements from the GDPR.

competency_questions_evaluated.xlsx is the Excel file which contain all competency questions from GDPR statements that are related to data sharing. With explanation of gap, label generated and original statement from GDPR.

aiact_gdpr_extracted_statements.xlsx is the Excel file which contain all competency questions and original statements from GDPR. This Excel file is used to know if competency questions are related to data sharing.
