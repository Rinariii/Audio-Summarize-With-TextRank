from search import *
jabar_graph = UndirectedGraph(dict(
    Tasikmalaya=dict(Pangandaran=8, Garut=8),
    Sumedang=dict(Majalengka=5),
    Sukabumi=dict(Cianjur=15),
    Subang=dict(Sumedang=10, Indramayu=10),
    Kuningan=dict(Majalengka=10, Ciamis=8),
    Karawang=dict(Subang=8, Purwakarta=8),
    Indramayu=dict(Cirebon=8),
    Garut=dict(Bandung=8),
    Cirebon=dict(Kuningan=8),
    Cianjur=dict(West_Bandung=8, Purwakarta=8, Bandung=8),
    Ciamis=dict(Tasikmalaya=5, Pangandaran=5),
    Bogor=dict(Sukabumi=15, Cianjur=8, Bekasi=10),
    Bekasi=dict(Karawang=10),
    Bandung=dict(West_Bandung=5, Sumedang=10)
))

problem = GraphProblem('Bogor', 'Pangandaran', jabar_graph)
bfs_node = breadth_first_graph_search(problem)
dfs_node = depth_first_graph_search(problem)
ucs_node = uniform_cost_search(problem)

print("BFS :", breadth_first_graph_search(problem).solution())
print("DFS :", depth_first_graph_search(problem).solution())
print("UCS :", uniform_cost_search(problem).solution())
print("BFS Cost:", bfs_node.path_cost)
print("DFS Cost:", dfs_node.path_cost)
print("UCS Cost:", ucs_node.path_cost)