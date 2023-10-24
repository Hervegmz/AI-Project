import rdflib
import pandas as pd

g = rdflib.ConjunctiveGraph()

skos = rdflib.Namespace("http://www.w3.org/2004/02/skos/core#")
rdf = rdflib.Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
owl = rdflib.Namespace("http://www.w3.org/2002/07/owl#")
rdfs = rdflib.Namespace("http://www.w3.org/2000/01/rdf-schema#")
aia = rdflib.Namespace("aia:")
gdpr = rdflib.Namespace("gdpr:")

df = pd.read_excel("chat_history3.xlsx")

for index, row in df.iterrows():
    question = row['Question']
    #aia_ID = aia[name]
    #first_descriptors = row['Descriptors'].split(',')[0].strip(" []'\" ")
    unique_id = f"{row['AI Act statement']}"
    ai_point = rdflib.URIRef(unique_id)
    heading = row['Label']
    heading = heading.replace(" ","_")
    heading = rdflib.URIRef(heading)
    g.add((heading, rdf.type, skos.Concept,rdflib.Literal(heading,lang="en")))
    g.add((heading, skos.definition, rdflib.Literal(question, lang="en")))
    g.add((heading, skos.definition, rdflib.Literal(ai_point, lang="en")))
    
    '''subject2 = row['GDPR_ID']
    gdpr_ID = gdpr[subject2]
    second_id = f"{row['GDPR Point']}"
    gdpr_point = rdflib.URIRef(second_id)
    g.add((gdpr_ID, rdf.type, skos.Concept))
    g.add((gdpr_ID, rdfs.prefLabel, rdflib.Literal(first_descriptors, lang="en")))
    g.add((gdpr_ID, skos.definition, rdflib.Literal(gdpr_point, lang="en")))
    
    g.add((aia_ID,rdf.narrow,gdpr_ID))
    labels = [label.strip(" ['\"'] ") for label in row['Descriptors'].split(',')[1:]]
    
    for index2,label in enumerate(labels):
        close_match = skos.closeMatch
        g.add((aia_ID, rdfs.label, rdflib.Literal(label, lang="en")))
        g.add((gdpr_ID, rdfs.label, rdflib.Literal(label, lang="en")))'''

g.serialize("RDF_questions_test.ttl",format="turtle")
