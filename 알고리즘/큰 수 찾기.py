n,m,k = map(int, input().split())
arr=list(map(int, input().split()))
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
bubble_sort(arr)

first=arr[n-1]
second=arr[n-2]
result=0
while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m-=1
    if m==0:
        break
    result += second
    m -= 1
print(result)