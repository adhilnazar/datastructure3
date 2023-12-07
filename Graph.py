def add_node(v):
    global count_node
    if v not in node:
        node.append(v)

    for i in graph:
        i.append(0)

    temp = []
    for i in range(count_node):
        temp.append(0)
    graph.append(temp)
    
def printGraph():
    for i in range(count_node):
        for j in range(count_node):
            print(graph[i][j])

node = []
graph = []
count_node = 0
add_node(1)
printGraph()