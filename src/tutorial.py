from src.graph import create_graph, get_degree, dfs_traversal, bfs_traversal, find_shortest_path, visualize_graph

edges = [(1, 2), (2, 3), (3, 4), (3, 5), (5, 2), (2, 4)]

node = start = source = 1
target = 5
G = create_graph(edges)

create_graph(edges)
get_degree(G, node)
dfs_traversal(G, start)
bfs_traversal(G, start)
find_shortest_path(G, source, target)
visualize_graph(G)
