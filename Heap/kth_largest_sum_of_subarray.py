'''
Problem statement
Given an array of integers, find the Kth largest sum subarray For example, given the array [1, -2, 3, -4, 5] and K = 2, 
the 2nd largest sum subarray would be [3, -4, 5], which has a sum of 4.

Please note that a subarray is the sequence of consecutive elements of the array.

Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1 :
2
3 3
3 -2 5
2 2
4 1
Sample output 1 :
3
4
Explanation of Sample output 1 :
For the first test case, 
Sum of [0, 0] = 3
Sum of [0, 1] = 1
Sum of [0, 2] = 6
Sum of [1, 1] = -2
Sum of [1, 2] = 3
Sum of [2, 2] = 5
All sum of subarrays are {6, 5, 3, 3, 1, -2} where the third largest element is 3.

For the second test case, 
Sum of [0, 0] = 4
Sum of [0, 1] = 5
Sum of [1, 1] = 1
All sum of subarrays are {5, 4, 1} where the second largest element is 4.
Sample Input 2 :
2
4 10
5 4 -8 6
3 1
1 2 3
Sample output 2 :
-8
6
Explanation of Sample output 2 :
For the first test case, among the sum of all the subarray, the tenth-largest sum will be -8.

For the second test case, among the sum of all the subarray, the largest sum will be 6.
'''

import heapq

def getKthLargest(arr, k):
	#	Write your code here.
	n = len(arr)
	sums = []

	for i in range(n):
		curr_sum = 0
		# loop through each subarray to form the list of sum of all possible subarrays >>> eg at the end
		for j in range(i, n):
			curr_sum += arr[j]
			heapq.heappush(sums, curr_sum)
			# if len(sums) > k:
			# 	heapq.heappop(sums)
	while len(sums) != k:
		heapq.heappop(sums)
	return heapq.heappop(sums)



'''
for arr = [1, -2, 3, -4, 5]

subarrays are (starting from 1)-->> {1}, {1,-2} ,{1,-2,3}, {1,-2,3, -4}, and {1,-2,3, -4, 5}.
sums of these are [1, -1, 2, -2 , 7].

subarrays are (starting from -2)-->> {-2} ,{-2,3}, {-2,3,-4}, and {-2,3,-4, 5}.
sums of these are [-2, 1, -3, 2]

subarrays are (starting from 3)-->> {3}, {3,-4}, and {3,-4, 5}.
sums of these are [3, -1, 4]

and so on.....

for this at each point we have to keep track of curr_sum and add it to heap(sums)

At the end, we will get the max heap for all possible subarray's sum

'''