import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


def nx_chunk(graph, chunk_size):
    """
    Chunk a graph into subgraphs with the specified minimum chunk size.

    Inspired by Lukes algorithm.
    """

    # convert to a tree;
    # a balanced spanning tree would be preferable to a minimum spanning tree,
    # but networkx does not seem to have an implementation of that
    tree = nx.minimum_spanning_tree(graph)

    # select a root that is maximally far away from all leaves
    leaves = [node for node, degree in tree.degree() if degree == 1]
    minimum_distance_to_leaf = {node : tree.size() for node in tree.nodes()}
    for leaf in leaves:
        distances = nx.single_source_shortest_path_length(tree, leaf)
        for node, distance in distances.items():
            if distance < minimum_distance_to_leaf[node]:
                minimum_distance_to_leaf[node] = distance
    root = max(minimum_distance_to_leaf, key=minimum_distance_to_leaf.get)

    # make the tree directed and compute the total descendants of each node
    tree = nx.dfs_tree(tree, root)
    total_descendants = get_total_descendants(tree)

    # prune chunks, starting from the leaves
    chunks = []
    max_descendants = np.max(list(total_descendants.values()))
    while (max_descendants + 1 > chunk_size) & (tree.size() >= 2 * chunk_size):
        for node in list(nx.topological_sort(tree))[::-1]: # i.e. from leaf to root
            if (total_descendants[node] + 1) >= chunk_size:
                chunk = list(nx.descendants(tree, node))
                chunk.append(node)
                chunks.append(chunk)

                # update relevant data structures
                tree.remove_nodes_from(chunk)
                total_descendants = get_total_descendants(tree)
                max_descendants = np.max(list(total_descendants.values()))

                break

    # handle remainder
    chunks.append(list(tree.nodes()))

    return chunks


def get_total_descendants(dag):
    return {node : len(nx.descendants(dag, node)) for node in dag.nodes()}


fig, axes = plt.subplots(1, 3, figsize=(12, 4))

examples = nx.balanced_tree(2, 6), nx.random_powerlaw_tree(64), nx.karate_club_graph()

for g, ax in zip(examples, axes):
    chunks = nx_chunk(g, 5)
    node_to_color = dict()
    for ii, chunk in enumerate(chunks):
        for node in chunk:
            node_to_color[node] = ii
    nx.draw(g, node_color=[node_to_color[node] for node in g.nodes()], cmap='tab20', ax=ax)

plt.show()

for ii, chunk in enumerate(chunks):
    for node in chunk:
        node_to_color[node] = ii

nx.draw(g, node_color=[node_to_color[node] for node in g.nodes()], cmap='tab20')
plt.show()