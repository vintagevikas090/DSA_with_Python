'''Assuming 0 based indexing and initially all element are 1000'''

class min_Heap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.heap = [1000 for i in range(max_size)]

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
            if parent > val:
                self.swap_values(parent_index, index)
                index = parent_index
            else:
                # val is at it's correct position
                break

    def Min_Heapify(self, index):
        smallest = index
        left_index = 2*index + 1
        right_index = 2 * index + 2

        n = len(self.heap)

        if left_index < n and self.heap[left_index] < self.heap[smallest]:
            smallest = left_index
        
        if right_index < n and self.heap[right_index] < self.heap[smallest]:
            smallest = right_index

        if smallest != index:
            self.swap_values(smallest, index)
            self.Min_Heapify(smallest)

    def remove_ele(self):
        n = len(self.heap)
        if n == 0:
            print('Heap is Empty..')
        else:
            self.swap_values(0, n - 1)
            self.size -= 1
            temp = self.heap.pop()
            self.Min_Heapify(0)
            print(f"Removed element: {temp}")
    
    def print_heap(self):
        print('Heap: ')
        for i in self.heap:
            print(i, end = ' ')
        
h = min_Heap(7)
h.insert_in_heap(7)
h.insert_in_heap(3)
h.insert_in_heap(1)
h.insert_in_heap(6)
h.insert_in_heap(5)
h.insert_in_heap(4)
h.insert_in_heap(2)
# h.insert_in_heap(17)
h.print_heap()
print()
print(h.size)
print()
(h.remove_ele())
(h.remove_ele())
(h.remove_ele())
(h.remove_ele())
(h.remove_ele())
h.print_heap()

