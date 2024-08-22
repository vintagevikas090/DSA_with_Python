'''

Given pointers to the head nodes of  linked lists that merge together at some point, find the node where the two lists merge.
The merge point is where both lists point to the same node, i.e. they reference the same memory location. It is guaranteed that the two head nodes will be different, and neither will be NULL. If the lists share a common node, return that node's  value.

Note: After the merge point, both lists will share the same node pointers.

Example

In the diagram below, the two lists converge at Node x:

[List #1] a--->b--->c
                     \
                      x--->y--->z--->NULL
                     /
     [List #2] p--->q


  '''

def findMergeNode(head1, head2):
    visited = []
    while head1 or head2:
        if head1:
            if head1 in visited:
                return head1.data
            else:
                visited.append(head1)
            head1 = head1.next
        
        if head2:
            if head2 in visited:
                return head2.data
            else:
                visited.append(head2)
            head2 = head2.next 
