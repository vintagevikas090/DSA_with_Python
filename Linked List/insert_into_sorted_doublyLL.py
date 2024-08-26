'''
Given a reference to the head of a doubly-linked list and an integer, , create a new DoublyLinkedListNode object having data value  and insert it at the proper location to maintain the sort.

Example

 refers to the list 

Return a reference to the new list: .

Function Description

Complete the sortedInsert function in the editor below.

sortedInsert has two parameters:

DoublyLinkedListNode pointer head: a reference to the head of a doubly-linked list

int data: An integer denoting the value of the  field for the DoublyLinkedListNode you must insert into the list.

Returns

DoublyLinkedListNode pointer: a reference to the head of the list


'''

def sortedInsert(head, data):
    # Write your code here
    new_node = DoublyLinkedListNode(data)
    if head is None:
        return new_node
    
    temp = head
    prv = None
    while temp is not None:
        if temp.data >= data:
            if prv is None:
                new_node.next = temp
                temp.prev = new_node
                return new_node
            new_node.next = temp
            temp.prev = new_node
            prv.next = new_node
            new_node.prev = prv
            return head
        prv = temp
        temp = temp.next
    
    if temp is None:
        prv.next = new_node
        new_node.prev = prv
    return head
