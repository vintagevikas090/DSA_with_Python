'''
calculate the running median for a given array at every point

----> median is the mid element in the sorted array

eg.. arr = [6, 2, 1, 3, 7, 5]
think like each element is getting added one by one

first med is 6, second is  (6+2)// 2=3, third is 2 and so on.....

'''


import heapq

# for max Heap implementation
class Element:
    def __init__(self, value) -> None:
        self.value = value

    def __lt__(self, o) -> bool:
        return self.value > o.value

    def __eq__(self, __o: object) -> bool:
        return self.value == __o.value


# if the left and right half are unbalanced
def balance(lh, rh) -> None:
    l_l = len(lh)
    r_l = len(rh)
    if l_l == r_l or l_l == r_l+1:
        return
    
    if l_l > r_l:
        ele = heapq.heappop(lh) # Element class
        heapq.heappush(rh, ele.value)
    else:
        ele = heapq.heappop(rh) # int
        heapq.heappush(lh, Element(ele))


def findMedian(arr, n):
    lh = []
    rh = []
    ans = []

    for i in range(n):
        # if we are inserting the first ele
        if len(lh) == 0:
            heapq.heappush(lh, Element(arr[i]))
        else:
            top = lh[0] # since we don't know whether to remove it or not
            if arr[i] < top.value:
                heapq.heappush(lh, Element(arr[i]))
            else:
                heapq.heappush(rh, arr[i])
            balance(lh, rh)

        if i % 2 == 0:
            # if the index no is even, no of ele is odd
            curr_median = lh[0].value   # don't remove
        else:
            # even no of elements
            curr_median = (lh[0].value + rh[0]) // 2
        ans.append(curr_median)

    return ans


res = findMedian([6, 2, 1, 3, 7, 5], 6)
print(*res)