'''
Problem statement
Given an array of integers, check whether it represents max-heap or not. 
Return true if the given array represents max-heap, else return false.
'''

def checkMaxHeap(arr):
    n = len(arr)

    # Check each parent node
    # since after n // 2 --->>> all nodes are leaf nodes
    for i in range(n // 2):
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and arr[left_child] > arr[i]:
            return False

        if right_child < n and arr[right_child] > arr[i]:
            return False

    return True


# Main Code
n=int(input('Number of ele: '))
print('Enter the list element: ')
lst=[(int(i) for i in input().strip())]

if checkMaxHeap(lst):
    print('true')
else:
    print('false')
