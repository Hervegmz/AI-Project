import kglab
from pyvis.network import Network

kg = kglab.KnowledgeGraph()

kg.load_rdf("RDF_questions.ttl", format="turtle")

measure = kglab.Measure()
measure.measure_graph(kg)

ttl = kg.save_rdf_text()

VIS_STYLE = {
    "skos":{
        "color": "blue",
        "size": 40
    }
}
subgraph = kglab.SubgraphTensor(kg)
pyvis_graph = subgraph.build_pyvis_graph(notebook=True, style=VIS_STYLE)
  
pyvis_graph.force_atlas_2based()
pyvis_graph.show_buttons()
pyvis_graph.show("RDF_questions.html")

