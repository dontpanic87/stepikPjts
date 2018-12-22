graph = {}
n = int(input())
for i in range(n):
    k = input().split(' : ')
    if len(k) > 1:
        kk = str(k[1]).split()
        graph.setdefault(k[0], kk)
    else:
        graph.setdefault(k[0], [])

def bfs(graph, end, start):
    if end not in graph:
        return False
    elif start not in graph:
        graph.update({start: []})
        pass
    elif start == end:
        return True
    else:
        path = []
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in path:
                path.append(vertex)
                queue.extend(graph[vertex])
        if end in path: 
            return True
        else: 
            return False
        
res = []
q = int(input())
for i in range(q):
    k = input().split()
    if bfs(graph, k[0], k[1]):
        res.append('Yes')
    else:
        res.append('No')
for i in res:
    print(i)