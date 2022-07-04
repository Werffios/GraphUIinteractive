# function to create and return graph
import networkx as nx
from matplotlib import pyplot as plt


def create_graph(graph_type, num_nodes, num_edges):
    if graph_type == 'complete':
        G = nx.complete_graph(num_nodes)
    elif graph_type == 'random':
        G = nx.random_graphs.barabasi_albert_graph(num_nodes, num_edges)
    elif graph_type == 'erdos':
        G = nx.random_graphs.erdos_renyi_graph(num_nodes, num_edges)
    elif graph_type == 'watts':
        G = nx.random_graphs.watts_strogatz_graph(num_nodes, num_edges)
    elif graph_type == 'barabasi':
        G = nx.random_graphs.barabasi_albert_graph(num_nodes, num_edges)
    elif graph_type == 'newman':
        G = nx.random_graphs.newman_watts_strog
    return G
# test create_graph()
G = create_graph('complete', 10, 0)
# create partition
def create_partition(graph, num_groups):
    information = []
    partition_1, partition_2 = nx.algorithms.community.kernighan_lin_bisection(graph)
    subgraph_1, subgraph_2 = graph.subgraph(partition_1), graph.subgraph(partition_2)
    print(partition_1)
    print(subgraph_1.edges())
    print(subgraph_2.edges())
    for i in subgraph_1.edges():
        print(i, end=' ')
        if not i in G.edges():
            information.append(i)
    print(information)
    nx.draw(subgraph_1)
    plt.show()
    nx.draw(subgraph_2)
    plt.show()



create_partition(G, 2)