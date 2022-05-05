import morph_kgc
import os
import wget

#clean old mapping
os.system("rm mapping.ttl")

# download mapping
url='https://raw.githubusercontent.com/jatoledo/KG/main/mapping.ttl'
wget.download(url)

#generate log from Docker inspect
os.system("docker inspect $(docker images -a -q) >data.json")


# configuration file

config = """
[CONFIGURATION]
output_dir=
output_file=result

[DataSourceJSON]
file_path=data.json
mappings=mapping.ttl"""
# generate the triples and load them to an RDFlib graph
graph = morph_kgc.materialize(config)


# work with the graph
graph.query(' SELECT DISTINCT ?classes WHERE { ?s a ?classes } ')
graph.serialize(destination='result.ttl', format='turtle')

#os.system("java -jar rmlmapper-4.15.0-r361-all.jar  -m mapping.ttl -o result.ttl")
# Sparql query

import rdflib

g = rdflib.Graph()
g.parse("result.ttl",format="turtle")

knows_query = """
SELECT *
WHERE {
    ?s ?p ?o.

}"""

qres = g.query(knows_query)
for row in qres:
    print(f"{row.s}")
