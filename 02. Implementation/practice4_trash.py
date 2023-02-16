# 게임 개발 118p

n, m=map(int, input().split())

arr=[[0 for i in range(m)] for j in range(n)]

x, y, direct=map(int, input().split())
x-=1
y-=1
have_arr=[]

for i in range(n):
    temp_arr=list(map(int, input().split()))
    for j in range(len(temp_arr)):
        arr[i][j]=temp_arr[j]

for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j], end='')
    print()


direction=[[-1,0],[0,-1],[1,0],[0,1]]
stop_next=False;
exit_=False;
while exit_==False:
    # print('첫번째 while')
    turn_count=0
    while True:
        # print('두번째 while')
        # print('x= ', x+direction[direct][0], 'y= ',y+direction[direct][1], 'arr[x,y]= ', arr[x+direction[direct][0]][y+direction[direct][1]])
        temp_x=x+direction[direct][0]
        temp_y=y+direction[direct][1]
        
        if (temp_x>=0 and temp_x<m and temp_y>=0 and temp_y<n) and (arr[temp_x][temp_y]==1 or (temp_x,temp_y) in have_arr):
            print('회전')
            direct+=1
            turn_count+=1
            if direct>=4:
                direct=0
                # print('direct 0으로 초기화')
            if turn_count==4:
                if stop_next==True:
                    print('종료')
                    exit_=True
                    break
                stop_next=True
                x+=direction[(direct+2)%4][0]
                y+=direction[(direct+2)%4][1]
                break
            x+=direction[direct][0]
            y+=direction[direct][1]
            have_arr.append((x,y))
            direct+=1
            print(x,',',y)
        else:
            break

print(len(have_arr))
