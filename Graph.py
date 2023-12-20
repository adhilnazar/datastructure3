def add_node(v):
    global count_node
    if v not in node:
        node.append(v)
        count_node += 1
    for i in graph:
        i.append(0)
    temp = []
    for i in range(count_node):
        temp.append(0)
    graph.append(temp)

def add_edge(v1,v2):
    if v1 not in node:
        print("Can't do this operation")     
    elif v2 not in node:
         print("Can't do this operation")
    else:
        index1 = node.index(v1)
        index2 = node.index(v2)
        graph[index1][index2] = 1
        graph[index2][index1] = 1

def delete_node(v):
    if v not in node:
        return
    else:

        index = node.index(v)

        del graph[index]

        for row in graph:
            del row[index]

        global count_node
        count_node -= 1
        node.remove(v)
    
def printGraph():
    for i in range(count_node):
        for j in range(count_node):
            print(graph[i][j],end=" ")
        print()

node = []
graph = []
count_node = 0

add_node(1)
add_node(2)
add_node(3)
# delete_node(2)
add_edge(1,2) 
add_edge(1,3)
add_edge(3,2)
print(node)
printGraph()