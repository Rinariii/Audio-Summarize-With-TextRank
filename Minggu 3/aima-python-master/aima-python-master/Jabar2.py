from search import *

jabar_graph = UndirectedGraph(dict(
    Bekasi=dict(Karawang=10, Bogor=10),
    Karawang=dict(Purwakarta=8, Subang=8),
    Subang=dict(Purwakarta=8, Sumedang=10, Indramayu=10),
    Bogor=dict(Sukabumi=15, Cianjur=8),
    Sukabumi=dict(Cianjur=15),
    Purwakarta=dict(Cianjur=8),
    Cianjur=dict(West_Bandung=8, Bandung=8),
    West_Bandung=dict(Bandung=5),
    Bandung=dict(Garut=8, Sumedang=10),
    Sumedang=dict(Majalengka=5),
    Garut=dict(Tasikmalaya=8),
    Tasikmalaya=dict(Ciamis=5, Pangandaran=8),
    Indramayu=dict(Cirebon=8),
    Cirebon=dict(Kuningan=8),
    Majalengka=dict(Kuningan=10),
    Kuningan=dict(Ciamis=8),
    Pangandaran=dict(Ciamis=5)
))

jabar_graph.locations = dict(
    Bekasi=(10, 50), Karawang=(20, 50), Subang=(20, 40), Bogor=(20, 30),
    Bandung=(30, 10), Tasikmalaya=(45, 5), Ciamis=(50, 20), Majalengka=(40, 20),
    Sumedang=(35, 25), Purwakarta=(30, 30), Sukabumi=(20, 20), Cianjur=(23, 20),
    West_Bandung=(25, 10), Garut=(40, 5), Pangandaran=(50, 5), Kuningan=(45, 20),
    Cirebon=(45, 30), Indramayu=(40, 30)
)

problem = GraphProblem('Bogor', 'Pangandaran', jabar_graph)

greedy_goal = greedy_best_first_graph_search(problem, f=lambda n: problem.h(n))
path_greedy = [n.state for n in greedy_goal.path()]
cost_greedy = greedy_goal.path_cost

astar_goal = astar_search(problem)
path_astar = [n.state for n in astar_goal.path()]
cost_astar = astar_goal.path_cost

print("Greedy :", path_greedy, "cost:", cost_greedy)
print("A*     :", path_astar,  "cost:", cost_astar)
