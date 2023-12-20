def max_heap(arr,n,i):
    largest = i
    left = (2*i)+1
    right = (2*i)+2
    if left < n and arr[largest] > arr[left]:
        largest = left
    if right < n and arr[largest] > arr[right]:
        largest = right
    if largest != i:
        arr[largest],arr[i] = arr[i],arr[largest]
        max_heap(arr,n,largest)

def heapsort(arr):
    for i in range((n-1)//2,-1,-1):
        max_heap(arr,n,i)

    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        max_heap(arr,i,0)

arr = [20,80,90,40,70,30,60,10,50]
n = len(arr)

heapsort(arr)
print(arr)  


