# 음료수 얼려 먹기 149p

n, m=map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    # 좌표가 그래프 범위를 넘어가면 False 반환
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    
    # 만약 0인 지점을 찾으면, 상하좌우로 인접해있는 0인 칸을 모두 1로 만들고 True 반환(재귀 사용)
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    
    # 시작 지점이 0이 아니면 False를 반환
    return False

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1

print(result)