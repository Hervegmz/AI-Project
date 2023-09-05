import pandas as pd

fichier1 = pd.read_excel('.\Excel\EuroVoc_copie2.xlsx',sheet_name='Sheet1')
#fichier2 = pd.read_excel('Eurovoc_2.xlsx',sheet_name='Sheet2')

fichier3 = pd.read_excel('.\Excel\eurovoc_export_en_modif.xlsx')
correspondance = dict(zip(fichier3['ID'], fichier3['PT']))
print(correspondance)

fichier1['Descriptors']=''
#fichier2['Descriptors']=''
for index, row in fichier1.iterrows():
    valeurs = row['Labels'].split(',')
    #print(valeurs)
    correspondances = []
    for valeur in valeurs:
        valeur =valeur.strip()
        valeur = valeur.replace('[', '').replace(']', '')
        valeur = int(valeur)
        #print(type(valeur))
        if valeur in correspondance:
            correspondances.append(correspondance[valeur])
        else:
            correspondances.append(None)
    #print(correspondances)
    fichier1.at[index, 'Descriptors'] = ''.join(str(correspondances))

'''for index, row in fichier2.iterrows():
    valeurs = row['Labels'].split(',')
    #print(valeurs)
    correspondances2 = []
    
    for valeur2 in valeurs:
        valeur2 =valeur2.strip()
        valeur2 = valeur2.replace('[', '').replace(']', '')
        valeur2 = int(valeur2)
        print(type(valeur2))
        # Supprimer les espaces autour de la valeur
        if valeur2 in correspondance:
            correspondances2.append(correspondance[valeur2])
        else:
            correspondances2.append(None)  # Si aucune correspondance trouvée, ajouter None
    print(correspondances2)
    # Mettre à jour la colonne 'Correspondance' avec les résultats
    fichier2.at[index, 'Descriptors'] = ''.join(str(correspondances2))
'''
with pd.ExcelWriter('.\Excel\EuroVoc_copie3.xlsx') as writer :
    fichier1.to_excel(writer)
    #fichier2.to_excel(writer,sheet_name='Sheet2')
