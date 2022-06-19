import networkx as nx
import pandas as pd
import json

from networkx.readwrite import json_graph

Node = nx.Graph()

Node.add_edge("a", "b", weight=0.6)
Node.add_edge("a", "c", weight=0.2)
Node.add_edge("c", "d", weight=0.1)
Node.add_edge("c", "e", weight=0.7)
Node.add_edge("c", "f", weight=0.9)
Node.add_edge("a", "d", weight=0.3)

s1 = json.dumps(json_graph.node_link_data(Node))

json = json.loads(s1)

with open('test_csv.csv', 'w') as f:
    for key in json.keys():
        f.write(key + "," + str(json[key]) + "\n")
    f.close()

graph_import = {}
with open('test_csv.csv', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        print(line[line.index(',') + 1:])
        if line[line.index(',') + 1:] == 'False':
            graph_import[line[:line.index(',')]] = False
        elif line[line.index(',') + 1:] == 'True':
            graph_import[line[:line.index(',')]] = True
        elif line[line.index(',') + 1:] == '{}':
            graph_import[line[:line.index(',')]] = {}
        else:
            if line[:line.index(',')] not in graph_import:
                graph_import[line[:line.index(',')]] = list()
            if line[:line.index(',')] == 'nodes':
                for data in line[line.index(',') + 1:].split(','):
                    graph_import[line[:line.index(',')]].append({data.split("'")[1]: data.split("'")[3]})
            else:
                for data in line[line.index(',') + 1:].replace("}, {", "}|{").split("|"):
                    temp = data.split("'")
                    graph_import[line[:line.index(',')]].append(
                        {temp[1]: float(temp[2].replace(':', '').replace(',', '')), temp[3]: temp[5], temp[7]: temp[9]})
    f.close()

print(json_graph.node_link_data(Node))
print(graph_import)

G = json_graph.node_link_graph(graph_import)
print(G.nodes())