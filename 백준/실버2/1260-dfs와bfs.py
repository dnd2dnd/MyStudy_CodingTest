n,m,v=map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n+1):
    graph[i].sort()

print(graph)

def dfs(graph, start_node, visited=[]):
    dfs_str=''
    visited.append(start_node)
    for node in graph[start_node]:
        if node not in visited:
            dfs(graph, node, visited)

    for i in visited:
        dfs_str+=str(i)+' '
    return dfs_str

def bfs(graph, start_node):
    bfs_str=''    
    need_visited, visited = list(), list()
    need_visited.append(start_node)
    
    while need_visited:
        node = need_visited[0]
        del need_visited[0]
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    
    for i in visited:
        bfs_str+=str(i)+' '
    return bfs_str


print(dfs(graph, v))
print(bfs(graph, v))


from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, x, visited=[]):
    pr = ''
    visited.append(x)
    for node in graph[x]:
        if node not in visited:
            dfs(graph, node, visited)
    
    
    for i in visited:
        print(x, i)
        pr+=str(i)+' '
    return pr

def bfs(graph, x):
    queue = deque([x])
    visited = [x]

    while queue:
        now = queue.popleft()
        for node in graph[now]:
            if node not in visited:
                visited.append(node)    

    for i in visited:
        print(i, end=' ')

print(dfs(graph, v))
# bfs(graph, v)
