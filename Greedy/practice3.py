# 숫자카드게임 96p

row, col=map(int, input().split())

arr = [[0 for i in range(col)] for j in range(row)]

min_num=0
for i in range(row):
  arr[i]=list(map(int,input().split()))
  temp=min(arr[i])
  if temp>min_num:
    min_num=temp

print(min_num)