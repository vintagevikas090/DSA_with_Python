'''Assuming 0 based indexing and initially all element are 0'''

class max_Heap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.heap = [0 for i in range(max_size)]

    def swap_values(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def insert_in_heap(self, val):
        self.heap[self.size] = val
        self.size += 1
        index = self.size  - 1

        while index > 0:
            parent_index = (index-1)//2
            parent = self.heap[parent_index]
            # current = self.heap[index]  is same as val (throughout the iteration)
            if parent < val:
                self.swap_values(parent_index, index)
                index = parent_index
            else:
                # val is at it's correct position
                break

    def Max_Heapify(self, index):
        largest = index
        left_index = 2*index + 1
        right_index = 2 * index + 2

        n = len(self.heap)

        if left_index < n and self.heap[left_index] > self.heap[largest]:
            largest = left_index
        
        if right_index < n and self.heap[right_index] > self.heap[largest]:
            largest = right_index

        if largest != index:
            self.swap_values(largest, index)
            self.Max_Heapify(largest)

    def remove_ele(self):
        n = len(self.heap)
        if n == 0:
            print('Heap is Empty..')
        else:
            self.swap_values(0, n - 1)
            self.size -= 1
            temp = self.heap.pop()
            self.Max_Heapify(0)
            print(f"Removed element: {temp}")
    
    def print_heap(self):
        print('Heap: ')
        for i in self.heap:
            if i != 0:
                print(i, end = ' ')
        
h = max_Heap(10)
#2 6 8 5 4 3
h.insert_in_heap(2)
h.insert_in_heap(6)
h.insert_in_heap(8)
h.insert_in_heap(5)
h.insert_in_heap(4)
h.insert_in_heap(3)
# h.insert_in_heap(15)
# h.insert_in_heap(17)
h.print_heap()
# print()
# print(h.size)
# print()
# (h.remove_ele())
# (h.remove_ele())
# (h.remove_ele())
# (h.remove_ele())
# (h.remove_ele())
# h.print_heap()

