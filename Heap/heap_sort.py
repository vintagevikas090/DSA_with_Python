# max_heapify
def heapify(arr, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child

    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    # Build max heap using heapify
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # perform the steps of Deletion
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root with the last element
        heapify(arr, i, 0)

n = input()
arr = [int(ele) for ele in input().split()]
heapSort(arr)
# now arr is in ascending order
for ele in arr[::-1]:
    print(ele,end=' ')