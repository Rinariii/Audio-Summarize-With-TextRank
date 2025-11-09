from logic import *
from utils import *

#  Buat Knowledge Base
kb = PropKB()

# P = pit, B =  Breeze, S = Stench . W = Wumpus , G = Gold
P, B, S, W, G = {}, {}, {}, {}, {}
for x in range(1, 5):
    for y in range(1, 5):
        P[x, y] = expr(f"P_{x}_{y}") 
        B[x, y] = expr(f"B_{x}_{y}")  
        S[x, y] = expr(f"S_{x}_{y}")  
        W[x, y] = expr(f"W_{x}_{y}") 
        G[x, y] = expr(f"G_{x}_{y}") 

#  Aturan dunia Wumpus
kb.tell(expr("P_3_1 <=> (B_2_1 | B_4_1 | B_3_2)"))
kb.tell(expr("P_3_3 <=> (B_2_3 | B_4_3 | B_3_2 | B_3_4)"))
kb.tell(expr("P_4_4 <=> (B_3_4 | B_4_3)"))
kb.tell(expr("W_1_3 <=> (S_1_2 | S_1_4 | S_2_3)"))

#  Fact
for fact in ["P_3_1", "P_3_3", "P_4_4", "W_1_3", "G_2_3"]:
    kb.tell(expr(fact))

for fact in [
    "B_2_1", "B_2_3", "B_3_2", "B_3_4", "B_4_1", "B_4_3",
    "S_1_2", "S_1_4", "S_2_3"
]:
    kb.tell(expr(fact))

#  Fungsi ask if true
def tanya_aman(x, y):
    ada_pit = kb.ask_if_true(P[x, y])
    ada_wumpus = kb.ask_if_true(W[x, y])
    ada_gold = kb.ask_if_true(G[x, y])

    if ada_gold:
        print(f"({x},{y}) Ada Gold di sini! Ambil dan pulang!")
    elif not ada_pit and not ada_wumpus:
        print(f"({x},{y}) Aman untuk dikunjungi.")
    elif ada_pit:
        print(f"({x},{y}) Ada Pit")
    else :
        print(f"({x},{y}) Ada Wumpus")

# Tes Wumpus
tanya_aman(1,1)
tanya_aman(1,2)
tanya_aman(2,2)
tanya_aman(2,3)
