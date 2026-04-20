import sys, heapq
n, m = map(int, input().split())
'''
* 그래프 그리는 방법(자료구조에 담는 방법)
1) 2차원 배열에다가 (노드) 저장 (간선-1)
2) 노드는 노드대로, 간선은 간선대로 저장

node = adj
edges = 

'''

t = []
adj = [[] for _ in range(n + 1)]
edges = [0]
for i in range(1, m + 1):
    # 노드-간선 그래프를 자료구조로 담기
    nodeA, nodeB, temperature = map(int, input().split())
    adj[nodeA].append((nodeB, temperature, i)) # ()
    adj[nodeB].append((nodeA, temperature, i))
    edges.append(temperature)
    
adj[1].append((0, 0, 0))
'''
#adj
[
 [],
 [(2, 3, 1), (3, 6, 3)],
 [(1, 3, 1), (3, 2, 2), (4, 1, 6), (5, 10, 7)],
 [(2, 2, 2), (1, 6, 3), (4, 3, 4)],
 [(3, 3, 4), (5, 7, 5), (2, 1, 6)],
 [(4, 7, 5), (2, 10, 7)]
]
#edges = [0, 3, 2, 6, 3, 7, 1, 10]


'''


# distance
distance = [float('inf')] * (m + 1)
distance[0] = 0

# 우선순위큐로 문제 풀기
queue = []
heapq.heappush(queue, (0, 1, 0)) # cost, node, idx(edge)

while queue:
    cost, node, prev_idx = heapq.heappop(queue)
    if node == n:
        print(cost)
        break
    if cost > distance[prev_idx]:
        continue
    
    # cost가 제일 작은 거를 넣어주기!
    for next_node, temperature, next_idx in adj[node]:
        total_cost = cost + abs(edges[prev_idx] - temperature)
        if total_cost < distance[next_idx]:
            distance[next_idx] = total_cost
            heapq.heappush(queue, (total_cost, next_node, next_idx))
    
    