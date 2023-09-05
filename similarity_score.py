import pandas as pd
from transformers import BertTokenizer, BertModel
import torch
import pickle

def compute_similarity(text1, text2):
    from sklearn.metrics.pairwise import cosine_similarity
    import numpy as np

    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

    tokens1 = tokenizer(text1, return_tensors="pt")
    tokens2 = tokenizer(text2, return_tensors="pt")

    model = BertModel.from_pretrained("bert-base-uncased")
    with torch.no_grad():
        output1 = model(**tokens1)
        output2 = model(**tokens2)

    sentence_embedding1 = torch.mean(output1.last_hidden_state, dim=1)  # Average pooling
    sentence_embedding2 = torch.mean(output2.last_hidden_state, dim=1)

    cosine_sim = cosine_similarity(sentence_embedding1.numpy(), sentence_embedding2.numpy())

    # Return the similarity score instead of printing it
    return cosine_sim[0][0]

df = pd.read_excel(".\Excel\EuroVoc.xlsx",sheet_name='Sheet2')
dfnew=df.dropna(subset=["GDPR Point"])

model_name = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

with open('semantics_model.sav', 'rb') as file:
    loaded_model = pickle.load(file)
result =[]
max_score=0
for index,row in dfnew.iterrows():
    ai_point ="‘small-scale provider’ means a provider that is a micro or small enterprise within the meaning of Commission Recommendation 2003/361/EC 61 ;"
    current = row['GDPR Point']
    score = compute_similarity(ai_point,current)
    
    result.append((ai_point, current, score))
df_final=pd.DataFrame(result,columns=['AI Point','GDPR Point','Similarity_score'])
df_sorted = df_final.sort_values(by='Similarity_score',ascending=False)
print(df_final)

with pd.ExcelWriter('.\Excel\similarity_whole_ai.xlsx') as writer :
    df_final.to_excel(writer)
    df_sorted.to_excel(writer,sheet_name='sheet2')
