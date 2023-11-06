import rdflib
import pandas as pd
'''Python file use to convert data from excel to turtle format'''
g = rdflib.ConjunctiveGraph()

skos = rdflib.Namespace("http://www.w3.org/2004/02/skos/core#")
rdf = rdflib.Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
owl = rdflib.Namespace("http://www.w3.org/2002/07/owl#")
rdfs = rdflib.Namespace("http://www.w3.org/2000/01/rdf-schema#")
aia = rdflib.Namespace("aia:")
gdpr = rdflib.Namespace("gdpr:")

df = pd.read_excel("post_knowledge_graph.xlsx")

for index, row in df.iterrows():
    #name = row['Question']
    name="Data Sharing"
    name = name.replace(" ","_")
    question = rdflib.URIRef(name)
    #aia_ID = aia[name]
    #first_descriptors = row['Descriptors'].split(',')[0].strip(" []'\" ")
    unique_id = f"{row['Original Statement']}"
    gdpr_point = rdflib.URIRef(unique_id)
    heading = row['Label']
    g.add((question, rdf.type, skos.Concept,rdflib.Literal(question,lang="en")))
    g.add((question, rdfs.prefLabel, rdflib.Literal(heading, lang="en")))
    g.add((question, skos.definition, rdflib.Literal(gdpr_point, lang="en")))

g.serialize("RDF_questions.ttl",format="turtle")
