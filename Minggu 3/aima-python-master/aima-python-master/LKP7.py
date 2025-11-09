class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(parent, child):
        parent.children.append(child)


def dfs(node, target):
    print("Visit:", node.data)
    if node.data == target:
        return True
    for child in node.children:
        if dfs(child, target):
            return True
    return False


from collections import deque
def bfs(root, target):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print("Visit:", node.data)
        if node.data == target:
            return True
        for child in node.children:
            queue.append(child)
    return False

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")

A.add_child(B)
A.add_child(C)
B.add_child(D)
B.add_child(E)
C.add_child(F)
C.add_child(G)

print("DFS Method : ")
found_dfs = dfs(A, "E")
print("Found E?" , found_dfs)

print("\n BFS Method : ")
found_bfs = bfs(A, "E")
print("Found E?" , found_bfs)