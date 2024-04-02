import heapq
def kSmallest(lst, k):
    heapq.heapify(lst)
    res = []
    for i in range(k):
        res.append((heapq.heappop(lst)))
    return res
# Main Code
print('enter the values for list(space seperated): ')
lst=list(int(i) for i in input().strip().split(' '))
k=int(input('enter k: '))
ans=kSmallest(lst, k)
print(*ans, sep='\n')
