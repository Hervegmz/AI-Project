import rdflib
import pandas as pd

'''Python file use to convert data from excel to turtle format'''

g = rdflib.ConjunctiveGraph()

skos = rdflib.Namespace("http://www.w3.org/2004/02/skos/core#")
rdf = rdflib.Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
owl = rdflib.Namespace("http://www.w3.org/2002/07/owl#")
rdfs = rdflib.Namespace("http://www.w3.org/2000/01/rdf-schema#")

df = pd.read_excel(".\intermediate_excel_files\competency_questions_evaluated.xlsx",sheet_name="NO_answers")

for index, row in df.iterrows():
    name = row['Label']
    name = name.replace(" ","_")
    label = rdflib.URIRef(name)
    question_node = rdflib.URIRef(row['Question'].replace(" ", "_"))

    g.add((question_node, rdf.type, rdf.Property, rdflib.Literal(row['Question'], lang="en")))

    g.add((question_node, skos.definition, rdflib.Literal(f"{row['Original Statement']}", lang="en")))

    g.add((question_node, rdf.explanation, rdflib.Literal(row['Explanation'], lang="en")))

    g.add((label, rdf.type, skos.Concept))
    g.add((label, rdf.question, question_node))

# Serialize the graph to a Turtle file
g.serialize(".\extra\RDF_extra.ttl", format="turtle")

