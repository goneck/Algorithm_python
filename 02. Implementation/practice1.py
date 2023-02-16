# 구현 문제
# 완전탐색과 시뮬레이션 문제

# 상하좌우 문제 110p

n=int(input())
data=input().split() # str 형이므로 map과 list로 변환해주지 않아도 된다.

# arr=[[0 for i in range(n)] for j in range(n)]
now_x=1
now_y=1

for i in range(len(data)):
    if data[i]=="L":
      if now_y>1:
         now_y-=1
    elif data[i]=="R":
       if now_y<n:
          now_y+=1
          print("R")
    elif data[i]=="U":
       if now_x>1:
          now_x-=1
          print("U")
    elif data[i]=="D":
       if now_x<n:
          now_x+=1
          print("D")


print(now_x," ",now_y)
      
      
        
    







