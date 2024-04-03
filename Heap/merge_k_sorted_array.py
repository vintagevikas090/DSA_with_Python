import heapq

class Element:
    def __init__(self, val, index) -> None:
        self.val = val
        self.index = index

    def __lt__(self, o):
        return self.val < o.val

    def __eq__(self, o):
        return self.val == o.val
    

def merge_k_sorted_array(arr, k):
    ans = []
    #ptr for the all the arrays (initially at index 0 for all)
    ptr = [0 for i in range(k)]
    '''
    say ptr = [1,2,3]
    --> ptr[0] ->> means first array of 'arr' and   '1' means the 2nd ele.. i.e ptr[0] ->> 2nd ele of first array of arr
    '''

    # put all the first element of all inner list to heap  
    # eg.. arr[0][0] -->> first ele of 1st inner list
    heap = [Element(arr[i][0], i)  for i in range(k)]
    #convert into min heap
    heapq.heapify(heap)

    while len(heap) > 0:
        smallest = heapq.heappop(heap) # element class
        minVal = smallest.val
        ans.append(minVal)
        curr_idx = smallest.index # index of the array from which the element belongs

        # say curr_idx = 2 ----> so arr[curr_idx] -->> 2nd array in 'arr'    (since indexing start from 0)
        # ptr[2] -->> contains the index of the element popped(smallest)
        # therefore  ptr[2]+ 1  -- > points to next element's index of 2nd array
        if ptr[curr_idx] + 1 < len(arr[curr_idx]):#if we are not at end of this array
            ptr[curr_idx] += 1
            next_ele = Element(arr[curr_idx][ptr[curr_idx]], curr_idx)
            #add the next element from other array to heap
            heapq.heappush(heap, next_ele)

    return ans
            

l = [[2, 4, 5, 6], [1, 3], [1, 2, 7]]
res = merge_k_sorted_array(l, 3)
print(*res)