# Selection Sort 선택 정렬
# 매번 가장 작은 것을 선택해서 앞으로 보내는 정렬(정확히는 교환임), 가장 원시적인 방법
# 시간복잡도 O(N^2)

# Insertion Sort 삽입 정렬
# 1번째 인덱스부터 시작
# 비교할 인덱스의 숫자를 앞의 인덱스부터 0번째 인덱스까지 비교하며 자신보다 더 작은 숫자가 나올때까지 교환
# 시간복잡도 O(N^2) 최선의 경우에는 O(N) == 리스트가 거의 정렬되어 있는 상태라면 매우 빠르게 동작
# 정렬 된 리스트의 경우는 퀵정렬이나 다른 정렬 알고리즘보다 삽입 정렬이 빠르다

# Quick Sort 퀵 정렬
# 가장 많이 사용되는 정렬 알고리즘
# 기준 데이터보다 작은 데이터와 큰 데이터의 위치를 바꿈
# Pivot==기준, 피벗을 설정하고 리스트를 분할하는 방법에 따라 퀵 정렬이 여러가지 방식으로 구분된다.
# 여기서 배울 건 호어 분할(Hoare Partition), 리스트의 첫 번째 데이터를 피벗으로 정하는 방식이다.
# 피벗을 설정한 뒤, 왼쪽에서부터 피벗보다 큰 데이터를 찾고, 오른쪽에서부터 피벗보다 작은 데이터를 찾는다.
# 큰 데이터와 작은 데이터의 위치를 교환한다.
# 비교하다 보면 왼쪽부터 찾는 값과 오른쪽부터 찾는 값이 교차하는 지점이 온다. 이 때 '작은 데이터'와 피벗을 교환한다.
# 결과적으로 피벗을 기준으로 왼쪽은 작은 데이터, 오른쪽은 큰 데이터로 나뉘게 된다. 이 작업을 '분할(Devide)' 혹은 '파티션(Partition)'이라고 한다.
# 피벗을 기준으로 나뉜 왼쪽과 오른쪽을 다시 각각 피벗을 설정하여 파티션을 진행한다. 
# 퀵 정렬은 재귀로 구현하며, 종료 조건은 현재 리스트의 데이터 수가 1개인 경우이다. 
# 평균 시간 복잡도 O(NlogN), 최악의 시간 복잡도 O(N^2) == 이미 데이터가 정렬되어 있는 경우

# 퀵정렬 소스코드
array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start>=end: # 원소가 한 개인 경우
        return
    pivot=start
    left=start+1
    right=end
    # 피벗보다 큰 데이터를 찾을 때까지 반복 (왼쪽 -> 오른쪽)
    while left<=end and array[left]<=array[pivot]:
        left+=1
    #피벗보다 작은 데이터를 찾을 때까지 반복 (오른쪽 -> 왼쪽)
    while right>start and array[right]>=array[pivot]:
        right-=1
    if left>right: # 왼 오 교차
        array[right], array[pivot]=array[pivot], array[right]
    else:
        array[left], array[right]=array[right], array[left]
    
    quick_sort(array,start,right-1)
    quick_sort(array,right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)

# 파이썬의 장점을 살린 퀵 정렬 소스코드
array2=[5,7,9,0,3,1,6,2,4,8]

def quick_sort2(array):
    if len(array)<=1:
        return array
    
    pivot=array[0]
    tail=array[1:]

    left_side=[x for x in tail if x<=pivot] # 분할된 왼쪽 리스트
    right_side=[x for x in tail if x>pivot] # 분할된 오른족 부분

    return quick_sort2(left_side)+[pivot]+quick_sort2(right_side)

print(quick_sort2(array2))

# Count Sort 계수 정렬
# 데이터 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 사용할 수 있으나 매우 빠른 정렬 알고리즘( 비교 기반의 알고리즘 X )
# 일반적으로 데이터 최대값과 최소값의 차가 1,000,000을 넘지 않는 경우 효과적,
# 모든 범위를 담을 수 있는 크기의 리스트를 선언해야 하기 때문
# 데이터 범위 크기의 0으로 이루어진 리스트를 선언하고 데이터 값과 동일한 인덱스의 데이터를 1씩 증가시키고, 리스트의 인덱스 수를 데이터만큼 출력한다.
# 시간 복잡도 데이터의 개수가 N, 최대값이 K일 때 O(N+K)
# [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# [2,2,2,1,1,2,1,1,1,2]
# ==> 출력 : 0 0 1 1 2 3 4 4 ...


# 정렬 라이브러리 sorted() 병합 정렬 기반, 최악의 경우에도 시간 복잡도 O(NlogN) 보장
# 리스트, 딕셔너리 등을 입력받아도 반환되는 결과는 리스트 자료형
# result=sorted(array)
# sort()는 리스트를 반환하지 않고 리스트 자체를 바로 정렬해준다
# array.sort()

# key를 매개변수로 입력받을 수 있다. key 값으로는 하나의 함수가 들어가야 하며 정렬 기준이 된다.
# 리스트 데이터가 튜플로 구성되어 있을 때 각 데이터의 두 번째 원소를 기준으로 설정하는 경우
array=[('바나나',2),('사과',5),('당근',3)]
def setting(data):
    return data[1]

result=sorted(array, key=setting)
print(result)