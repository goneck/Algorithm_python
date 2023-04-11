# DFS/BFS 실버 2
'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
'''

# 먼저 인접 행렬을 생성한다.
n, m, v=map(int, input().split())
matrix=[[0]*(n+1) for i in range(n+1)]

# 방문한 곳을 체크하기 위해 배열을 선언한다.
visited=[0]*(n+1)

# 입력받은 두 값(ex 1,3) 위치에 1을 삽입한다.
for i in range(m):
    a, b=map(int, input().split())
    matrix[a][b]=matrix[b][a]=1

def dfs(v):
    visited[v]=1 # 방문한 곳은 1로 변경한다.
    print(v, end=' ')
    for i in range(1, n+1):
        # 정점 i를 아직 방문하지 않았고 v와 연결돼있다면 i에 대해 다시 dfs를 실행한다.
        if (visited[i]==0 and matrix[v][i]==1):
            dfs(i)

# bfs는 보통 queue로 구현한다
def bfs(v):
    # 방문할 곳을 순서대로 넣은 큐
    queue=[v]
    # dfs 먼저 수행해서 visited 배열이 1로 바뀌어 있으므로 0으로 변경해서 방문 체크를 한다.
    visited[v]=0
    
    # queue 안에 방문해야 할 곳이 남아있지 않을 때까지
    while queue:
        v=queue.pop(0)
        print(v, end=' ')
        for i in range(1, n+1):
            # 방문하지 않았고 v와 연결돼있으면 queue에 삽입
            if (visited[i]==1 and matrix[v][i]==1):
                queue.append(i)
                visited[i]=0

        # 1 먼저 방문  ->  queue에 2랑 3이 들어감
        # 2 다음 방문  -> queue에 4가 들어감
        # 3 방문 -> queue에 4만 남음
        # 4 방문 끝

dfs(v)
print()
bfs(v)
