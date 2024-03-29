'''
Problem statement
You want to buy a ticket for a well-known concert which is happening in your city. But the number of tickets available is limited. Hence the sponsors of the concert decided to sell tickets to customers based on some priority.

A queue is maintained for buying the tickets and every person is attached with a priority (an integer, 1 being the lowest priority).

The tickets are sold in the following manner -

1. The first person (pi) in the queue requests for the ticket.
2. If there is another person present in the queue who has higher priority than pi, 
then ask pi to move at end of the queue without giving him the ticket.
3. Otherwise, give him the ticket (and don't make him stand in queue again).
Giving a ticket to a person takes exactly 1 second and it takes no time for removing and adding a person to the queue.
 And you can assume that no new person joins the queue.

Given a list of priorities of N persons standing in the queue and the index of your priority (indexing starts from 0). 
Find and return the time it will take until you get the ticket.

Detailed explanation ( Input/output format, Notes, Images )
Constraints:
Time Limit: 1 sec
Sample Input 1 :
3
3 9 4
2
Sample Output 1 :
2
Sample Output 1 Explanation :
Person with priority 3 comes out. But there is a person with higher priority than him.
 So he goes and then stands in the queue at the end. Queue's status :  {9, 4, 3}. Time : 0 secs.
Next, the person with priority 9 comes out. And there is no person with higher priority than him.
 So he'll get the ticket. Queue's status :  {4, 3}. Time : 1 secs.
Next, the person with priority 4 comes out (which is you). And there is no person with higher priority than you. 
So you'll get the ticket. Time : 2 secs.
Sample Input 2 :
5
2 3 2 2 4
3
Sample Output 2 :
4
'''

from sys import stdin
import sys
import heapq
    
class Element:
    def __init__(self, index, priority):
        self.index = index
        self.priority = priority

    def __lt__(self, other):
        return self.priority > other.priority

    def __eq__(self, other):
        return self.priority == other.priority


def buyTicket(arr, n, k) : 
    # max heap for priotity
    priority_q = [Element(i, arr[i]) for i in range(len(arr))]
    heapq.heapify(priority_q)

    time = 1
    while len(priority_q) != 0:
        top = heapq.heappop(priority_q) # class element
        pr = top.priority
        idx = top.index
        if idx == k:
            return time
        else:
            time += 1

    return -1


#taking input using fast I/O
def takeInput() :
    print('Number of elements in queue: ')
    n = int(stdin.readline().strip())
    if n == 0 :
        return n, list(), int(stdin.readline().strip())
    print('Enter the priority list(space seperated): ')
    arr = list(map(int, stdin.readline().strip().split(" ")))
    print('Enter your place(index) in queue(Assume indexing from 0): ')
    k = int(stdin.readline().strip())
    return n, arr, k

#main
sys.setrecursionlimit(10**6)
n, arr, k = takeInput()
print('Time taken is: ')
print(buyTicket(arr, n, k))
