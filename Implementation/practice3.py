# 왕실의 나이트 115p

data=input()
row=int(data[1])
column=int(ord(data[0]))-int(ord('a'))+1

steps=[[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]

count=0
for step in steps:
    if row+step[0]>=1 and row+step[0]<=8 and column+step[1]>=1 and column+step[1]<=8:
        count+=1

print(count)
