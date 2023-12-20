def add_node(v):
    if v not in graph:
        graph[v] = []

def add_edge(vertex1, vertex2):
    if vertex1 in graph:
        graph[vertex1].append(vertex2)
    else:
        graph[vertex1] = [vertex2]

    # If the graph is undirected, add the reverse edge as well
    if vertex2 in graph:
        graph[vertex2].append(vertex1)
    else:
        graph[vertex2] = [vertex1]

def delete_node(v):
    if v in graph:
        del graph[v]

    for i in graph:
        if v in graph[i]:
            graph[i].remove(v)    

def delete_edge(v1,v2):
    if v1 in graph and v2 in graph[v1]:
        graph[v1].remove(v2)
# if it is undirected graph
 
    if v2 in graph and v1 in graph[v2]:
        graph[v2].remove(v1)

def DFS(node,visited,graph):

    if node not in graph:
        print("Error 404")
        return
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)
# def bfs_itr(snode,graph):
#     visited=set()
#     if snode not in graph:
#         return None
#     qeue=[snode]
#     while qeue:
#         curr=qeue.pop(0)
#         if curr not in visited:
#             print(curr)
#             visited.add(curr)
#             for x in graph[curr]:
#                 if x not in visited:
#                     qeue.append(x)

def BFS(node,graph):

    visited = set()
    
    if node not in graph:
        return 404 
    queue = [node]
    while queue:
        curr = queue.pop(0)
        if curr not in visited:
            print(curr)
            visited.add(curr)
            for x in graph[curr]:
                if x not in visited:
                    queue.append(x)
                    

graph = {}
visited = set()
add_node(1)
add_node(2)
add_node(3)
add_node(4)
add_node(5)
add_edge(1,4)
add_edge(1,2)
add_edge(3,4)
add_edge(4,5)
add_edge(5,1)
add_edge(5,2)
# delete_node(3)

# delete_edge(2,5)
# DFS(5,visited,graph)
# bfs_itr(3,graph)
print(graph)