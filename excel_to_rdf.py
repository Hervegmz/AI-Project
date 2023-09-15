from rdflib import ConjunctiveGraph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS
import pandas as pd

df = pd.read_excel(".\Excel\EuroVoc_firstpart.xlsx")
g = ConjunctiveGraph()
tair = Namespace('http://tair.adaptcentre.ie/ontologies/tair/')
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
predicates = [
    tair.decomposes,
    skos.definition,
    skos.altLabel,
    #tair.constrainedBy
]

for index, row in df.iterrows():
    subject = URIRef(row['Subject'])  
    unique_id = f"{row['AI Point']}"
    ai_point = URIRef(unique_id)
    collection = Literal(row['Collection'])
    descriptors = Literal(row['Descriptors'])
    #constrain = Literal(row['Constrained'])
    objects = {
        skos.definition:ai_point,
        skos.altLabel:descriptors,
        tair.decomposes:collection,
     #   tair.constrainedBy:constrain
    }
    for predicate in predicates:
        object_literal = Literal(objects[predicate])
        
        g.add((subject, predicate, object_literal))
   
g.serialize('testTriples.ttl', format='turtle')

'''for index, row in df.iterrows():
    unique_id = f"{row['AI Point']}"
    unique_id = unique_id.replace(" ","_")
    second_id = f"{row['GDPR Point']}"
    second_id = second_id.replace(" ","_")
    ai_point = URIRef(unique_id)
    
    gdpr_point = URIRef(second_id)
    descriptors = Literal(row['Descriptors'])
    
    g.add((ai_point, RDF.type, tair['AIPoint']))
    g.add((ai_point, RDFS.label, Literal('AI Point')))
    g.add((ai_point, tair['hasGDPRPoint'], gdpr_point))
    g.add((ai_point, tair['hasDescriptors'], descriptors))
    
    g.add((gdpr_point, RDF.type, tair['GDPRPoint']))
    g.add((gdpr_point, RDFS.label, Literal('GDPR Point')))
    g.add((gdpr_point, tair['hasAIPoint'], ai_point))
    g.add((gdpr_point, tair['hasDescriptors'], descriptors))
    
    g.add((descriptors, RDF.type, tair['Descriptors']))
    g.add((descriptors, RDFS.label, Literal('Descriptors')))
    g.add((descriptors, tair['belongsToAIPoint'], ai_point))
    g.add((descriptors, tair['belongsToGDPRPoint'], gdpr_point))
    
    g.add((ai_point,descriptors,gdpr_point))'''

