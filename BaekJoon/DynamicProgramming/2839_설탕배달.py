# 다이나믹 프로그래밍 실버4
import math

# 3<=N<=5000

n=int(input())
answer=0
end=False

# 1. 5로만 나누어 떨어지는 경우
if (n%5==0):
    answer=n/5
    end=True
# 2. 5와 3으로 나누어 떨어지는 경우
else:
    for i in range(int(math.floor(n/5)), 0, -1):
      # print("i=",i)
      if (n-(5*i))%3==0:
        # print('break')
        answer+=i
        answer+=(n-(5*i))/3
        end=True
        break
# 3. 3으로만 나누어 떨어지는 경우
if end==False:
  if (n%3==0):
    answer=n/3
  # 4. 5와 3 둘 다로 나누어 떨어지지 않는 경우
  else: answer=-1

print(int(answer))