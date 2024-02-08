class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

max_size = 10
class SLL:
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return(self.head == None)
    
    def isFull(self):
        return(self.count == max_size)

    def insertAtHead(self, d):
        if(self.isFull()):
            return False
        nn = Node(d)
        if(self.head == None):
            self.head = nn
        else:
            nn.next = self.head
            self.head = nn
        self.count += 1
        return True
    
    def insertAtTail(self, d):
        if(self.isFull()):
            return False
        nn = Node(d)
        if(self.isEmpty()):
            self.head = nn
        else:
            temp = self.head
            while(temp.next!=None):
                temp = temp.next
            temp.next = nn
        self.count+=1
        return True
    
    def insertAtPos(self, pos, d):
        if(self.isFull() or pos<1 or pos>self.count):
            return False
        if pos == 1:
            return self.insertAtHead(d)
        elif pos == self.count:
            return self.insertAtTail(d)
        else:
            temp = self.head
            i = 1
            while(i<pos-1 and temp!=None):
                temp = temp.next
                i+=1
            if temp is None:
                return False
            nn = Node(d)
            nn.next = temp.next
            temp.next = nn
        self.count+=1
        return True
        
    def Print_List(self):
        temp = self.head
        while temp!= None:
            print(temp.data, end= " ")
            temp = temp.next
        print()
        print('printed successfully')

    def DeleteAtHead(self):
        if(self.isEmpty()):
            return False
        temp = self.head
        p = self.head.data
        if(self.count==1):
            self.head = None
        else:
            self.head = temp.next
            temp.next = None
        del temp
        self.count-=1
        return p

    def DeleteAtTail(self):
        if(self.isEmpty()):
            return False
        temp = self.head
        if(self.count==1):
            p = self.head.data
            self.head = None
            del temp
        else:
            while(temp.next.next !=None):
                temp = temp.next
            to_del = temp.next
            p = to_del.data
            temp.next = None
            del to_del
        self.count-=1
        return p
    
    def DeleteAtPos(self, pos):
        if(self.isEmpty() or pos<1 or pos>self.count):
            return False
        if pos == 1:
            return self.DeleteAtHead()
        elif pos == self.count:
            return self.DeleteAtTail()
        else:
            temp = self.head
            i = 1
            while(i<pos-1):
                temp = temp.next
                i+=1
            to_del = temp.next
            temp.next = to_del.next
            to_del.next = None
            p = to_del.data
            del to_del
        self.count-=1
        return p
    
    # to find if element is there or not
    def Search(self, val):
        if self.isEmpty():
            return False
        temp = self.head
        while temp!= None:
            if temp.data ==val :
                return True
            else:
                temp = temp.next
        return False

    # to Find the pos of a element
    def Find_pos(self, val):
        if self.isEmpty():
            return -1
        if self.Search(val):
            temp = self.head
            count = 1
            while(temp!=None):
                if temp.data == val:
                    return count
                else:
                    temp = temp.next
                count+=1
        else:
            return -1
            

s = SLL()
s.insertAtHead(5)
s.insertAtHead(10)
s.Print_List()
s.insertAtTail(0)
s.insertAtHead(15)
s.Print_List()
s.insertAtHead(-5)
s.insertAtPos(4, 20)
print("Created SLL is : ")
s.Print_List()
s.DeleteAtTail()
s.Print_List()
s.DeleteAtHead()
s.Print_List()
s.DeleteAtPos(2)
s.Print_List()
print(s.Search(15))
print(s.Find_pos(200))