import pandas as pd
from pyeurovoc import EuroVocBERT
import re

model = EuroVocBERT(lang="en")
df = pd.read_excel(".\Excel\EuroVoc_copie2.xlsx",sheet_name='Sheet1')
dfnew=df.dropna(subset=["AI Point"])
ai_point = []
result =[]
resultat=[]
gdpr_point=[]
similarity_score = []
df2=pd.read_excel(".\Excel\EuroVoc_copie2.xlsx",sheet_name='Sheet1')
dfnew2=df.dropna(subset=['GDPR Point'])
for index,row in dfnew.iterrows():
    labels=[]
    ai_point = row['AI Point']
    similarity_score = row['Similarity_score']
    prediction = model(ai_point,num_labels=4)
    for cellule in row:
        matches = re.findall("'(.*?)'", str(cellule))
        labels.extend(matches)
    print(labels)
    #labels = list(map(int, labels))
    result.append((similarity_score,ai_point,prediction,list(map(int,labels))))
for index,row in dfnew2.iterrows():
    labels2=[]
    gdpr_point = row['GDPR Point']
    prediction = model(gdpr_point,num_labels=4)
    for cellule in row:
            matches = re.findall("'(.*?)'", str(cellule))
            labels2.extend(matches)
    resultat.append((gdpr_point,prediction))
newdf = pd.DataFrame(result,columns=['Similarity_score','AI Point','Tags_ai','Labels'])
newdf2 = pd.DataFrame(resultat,columns=['GDPR Point','Tags_gdpr'])
with pd.ExcelWriter('.\Excel\EuroVoc_copie2.xlsx') as writer :
    newdf.to_excel(writer)
    newdf2.to_excel(writer,startcol=5)