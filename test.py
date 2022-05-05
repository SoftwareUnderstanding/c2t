import morph_kgc
import os
#generate log from Docker inspect
os.system("docker inspect $(docker images -a -q) >data.json")

# generate the triples and load them to an RDFlib graph
graph = morph_kgc.materialize('config.ini')

# work with the graph
graph.query(' SELECT DISTINCT ?classes WHERE { ?s a ?classes } ')
graph.serialize(destination='result.ttl', format='turtle')

# Sparql query

import rdflib

g = rdflib.Graph()
g.parse("result.ttl",format="turtle")

knows_query = """
SELECT *
WHERE {
    ?s a <https://w3id.org/docker/image/dockerObject>.

}"""

qres = g.query(knows_query)
for row in qres:
    print(f"imageID: {row.id}  has OS : {row.os}, author: {row.auth}")
