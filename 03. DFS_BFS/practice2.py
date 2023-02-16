# 미로 탈출 152p
from collections import deque

n, m=map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

# 상하좌우 (왼쪽 상단이 (0,0)이기 때문에)
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x, y=queue.popleft()

        # 현재 위치에서 4가지 방향을 검사
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            # 그래프 범위를 벗어났을 경우 무시
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            
            # 0일 경우 무시(괴물이 있는 경우)
            if graph[nx][ny]==0:
                continue
            
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
          
    return graph[n-1][m-1]

print(bfs(0,0))
        