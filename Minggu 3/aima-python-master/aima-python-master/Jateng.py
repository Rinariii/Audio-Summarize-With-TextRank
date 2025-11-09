from search import *

jateng_graph = UndirectedGraph(dict(
    Ambarawa=dict(Ungaran=10, Magelang=25),
    Batang=dict(Kendal=25, Pekalongan=30),
    Boyolali=dict(Salatiga=18, Solo=22),
    DesaA=dict(Magelang=40, Sragen=15, Solo=30),
    Kendal=dict(Semarang=20, Batang=25),
    Magelang=dict(Ambarawa=25, DesaA=40),
    Pekalongan=dict(),
    Salatiga=dict(Ungaran=20, Boyolali=18),
    Semarang=dict(Kendal=20, Ungaran=15),
    Solo=dict(Boyolali=22, Sragen=25, DesaA=30),
    Sragen=dict(Solo=25, DesaA=15),
    Ungaran=dict(Semarang=15, Ambarawa=10, Salatiga=20)
))



problem = GraphProblem('Semarang', 'DesaA', jateng_graph)
bfs_node = breadth_first_graph_search(problem)
dfs_node = depth_first_graph_search(problem)
ucs_node = uniform_cost_search(problem)

print("BFS :", breadth_first_graph_search(problem).solution())
print("DFS :", depth_first_graph_search(problem).solution())
print("UCS :", uniform_cost_search(problem).solution())
print("BFS Cost:", bfs_node.path_cost)
print("DFS Cost:", dfs_node.path_cost)
print("UCS Cost:", ucs_node.path_cost)