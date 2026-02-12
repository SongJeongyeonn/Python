N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

for nextNode, weight in graph[1]:
    print(f"next Node {nextNode}, weight = {weight}")
