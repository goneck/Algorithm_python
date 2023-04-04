# 다이나믹 프로그래밍 실버1

# 1. 현재 포도주와 이전 포도주를 마시는 경우 전전 포도주는 마시지 않음 따라서
# 따라서 d[i-3]에서(전전 포도주를 마시지 않았을 때의 최대값) a[i-1]과 a[i]를 더해줌 
# d[i]=d[i-3]+a[i-1]+a[i]

# 2.현재 포도주와 전전 포도주를 마시는 경우
# 이전 포도주는 마시지 않음
# 따라서 d[i]=d[i-2]+a[i]

# 3. 현재 포도주를 마시지 않는 경우
# d[i]=d[i-1]

n=int(input())
arr=[]

dp=[0]*n
if n==1:
    dp[0]=int(input())

elif n==2:
  dp[1]=int(input())+int(input())

else:
  for i in range(n):
     arr.append(int(input()))
  dp[0]=arr[0]
  dp[1]=arr[0]+arr[1]
  for i in range(2, len(arr)):
    dp[i]=max(dp[i-3]+arr[i-1]+arr[i], dp[i-2]+arr[i], dp[i-1])

print(dp[n-1])

