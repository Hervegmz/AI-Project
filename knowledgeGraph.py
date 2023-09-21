import kglab
from pyvis.network import Network

kg = kglab.KnowledgeGraph()

kg.load_rdf("RDF_firstpart.ttl", format="turtle")

measure = kglab.Measure()
measure.measure_graph(kg)

print("edges: {}\n".format(measure.get_edge_count()))
print("nodes: {}\n".format(measure.get_node_count()))

ttl = kg.save_rdf_text()
print(ttl)

VIS_STYLE = {
    "skos":{
        "color": "blue",
        "size": 40
    }
}

subgraph = kglab.SubgraphTensor(kg)
pyvis_graph = subgraph.build_pyvis_graph(notebook=True, style=VIS_STYLE)
  
pyvis_graph.force_atlas_2based()
pyvis_graph.show("RDF_firstpart.html")