'''
You are given 2 lists and integer k, you need to return the k maximum sum combinations
 that can be formed using the element from list (one from each)

 eg ..
 a = [1, 3, 5]
 b = [6, 4, 2]
 k = 2
 both list will be of same length

 output = [11, 9]
'''

'''We need the class for storing 'sum' and the indices from the two list, whose element sums up to 'sum' '''

import heapq
class Element:
    def __init__(self, val, id1, id2):
        self.val = val
        self.id1 = id1
        self.id2 = id2

    # for max heap, we need to override the inbuilt heap method
    def __lt__(self, other):
        return self.val > other.val
    
    def __eq__(self, other):
        return self.val == other.val


def k_max_sum_combinations(lst1, lst2, n, k):
    # sorting in the descending order (high to low)
    lst1.sort(reverse=True)
    lst2.sort(reverse=True)

    ans = []
    heap = [Element(lst1[0]+lst2[0], 0, 0)]
    taken = {}
    taken[(0,0)] = True # to avoid double counting

    for i in range(k):
        max_ele = heapq.heappop(heap) # class element 
        maxVal = max_ele.val
        ans.append(maxVal)

        # get the indices of the 'sum' you just appended
        idx1 = max_ele.id1
        idx2 = max_ele.id2

        #possibility 1
        if idx1 + 1 < n and not taken.get((idx1+1, idx2), False):
            curr_ele = Element(lst1[idx1+1]+lst2[idx2], idx1+1, idx2)
            heapq.heappush(heap, curr_ele)
            taken[(idx1+1, idx2)] = True

        # possibility 2
        if idx2 + 1 < n and not taken.get((idx1, idx2+1), False):
            curr_ele = Element(lst1[idx1]+lst2[idx2+1], idx1, idx2+1)
            heapq.heappush(heap, curr_ele)
            taken[(idx1, idx2+1)] = True

    return ans



a = [1, 3, 5]
b = [6, 4, 2]
result = k_max_sum_combinations(a, b, len(a), 2)
print(*result)