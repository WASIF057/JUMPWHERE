#Solution-1:
# def kth_largest(arr,k):
#     for i in range(k-1):
#         arr.remove(max(arr))
#     return max(arr)

#Solution-2:
# def kth_largest(arr,k):
#     n= len(arr)
#     arr.sort()
#     return arr[n-k]

#Solution-3:
import heapq

def kth_largest(arr,k):
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)

arr = [3,2,7,4,8,9,6,5]
k =3
print(kth_largest(arr,k))
