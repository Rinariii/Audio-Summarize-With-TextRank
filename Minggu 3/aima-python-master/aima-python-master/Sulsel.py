from search import *

sulsel_graph = UndirectedGraph(dict(
    BauBau=dict(Kendari=6, PasarB=4),
    Bira=dict(Jeneponto=3, Kendari=8),
    Jeneponto=dict(Makassar=4, Bira=3),
    Kendari=dict(Kolaka=5, Bira=8, BauBau=6),
    Kolaka=dict(Palopo=6, Kendari=5),
    Makassar=dict(ParePare=5, Jeneponto=4),
    Palopo=dict(ParePare=7, Kolaka=6),
    ParePare=dict(Makassar=5, Palopo=7),
    PasarB=dict(BauBau=4)
))




problem = GraphProblem('Makassar', 'PasarB', sulsel_graph)
bfs_node = breadth_first_graph_search(problem)
dfs_node = depth_first_graph_search(problem)
ucs_node = uniform_cost_search(problem)

print("BFS :", breadth_first_graph_search(problem).solution())
print("DFS :", depth_first_graph_search(problem).solution())
print("UCS :", uniform_cost_search(problem).solution())
print("BFS Cost:", bfs_node.path_cost)
print("DFS Cost:", dfs_node.path_cost)
print("UCS Cost:", ucs_node.path_cost)