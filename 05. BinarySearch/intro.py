# 이진탐색 Binary Search 
# 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘
# 범위를 절반씩 좁혀가며 데이터 탐색
# 위치를 나타내는 3개의 변수 사용 [ 시작점, 끝점, 중간점 ]
# 중간점이 실수일 때는 소수점 이하를 버린다. 중간점은 인덱스 숫자로 계산한다 ( 데이터 수=10, 시작점 인덱스=0, 끝점 인덱스=9일 경우 중간점은 4.5에서 0.5를 버려 4)
# 시간복잡도 O(log₂N) ==> O(logN)

# 재귀함수로 구현한 소스코드
def binary_search(array, target, start, end):
    if start>end:
        return None
    mid=(start+end)//2
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)
    
n, target=map(int, input().split())
array=list(map(int, input().split()))

result=binary_search(array, target, 0, n-1)
if result==None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1)

# 반복문으로 구현한 이진탐색 소스코드
def binary_search(array, target, start, end):
    print("반복문으로 구현")
    while start<=end:
        mid=(start+end)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None
    
n, target=list(map(int, input().split()))
array=list(map(int, input().split()))

result=binary_search(array, target, 0, n-1)
if result==None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1)

# 많은 양의 데이터를 시간 초과 없이 빠르게 입력 받기
# input() 사용 X X X
# sys.stdin.readline().rstrip() 사용 O O O
# rstrip() 함수는 줄 바꿈 기호로 입력된 엔터를 제거하는 역할이다.




