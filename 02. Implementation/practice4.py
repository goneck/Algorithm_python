n, m=map(int, input().split())

# 방문했던 위치 저장
d=[[0 for i in range(m)] for j in range(n)]

x, y, direction=map(int, input().split())
d[x][y]=1

# 전체 맵 정보
array=[]
for i in range(n):
    array.append(list(map(int, input().split())))

# 북동남서 방향 정의
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 왼쪽으로 회전하는 함수
# 왼쪽으로 회전하면 순서는 북(0)->서(3)->남(2)->동(1) 이므로 현재 방향에 -1씩 해주어야 한다
def turn_left():
    global direction
    direction-=1
    if direction==-1:
        direction=3
        

count=1
turn_time=0
while True:
    turn_left()
    nx=x+dx[direction] # next x
    ny=y+dy[direction] # next y

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny]==0 and array[nx][ny]==0:
        d[nx][ny]=1
        x=nx
        y=ny
        count+=1
        turn_time=0
        continue
    # 회전 후 가봤던 칸이거나 바다인 경우
    else:
        turn_time+=1
    if turn_time==4:
        nx=x-dx[direction]
        ny=y-dy[direction]

        if array[nx][ny]==0:
            x=nx
            y=ny
        else:
            break
        turn_time=0

print(count)
    
