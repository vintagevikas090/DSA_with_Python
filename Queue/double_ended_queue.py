'''Problem statement
You need to implement a class for Dequeue i.e. for double ended queue.
In this queue, elements can be inserted and deleted from both the ends.

You don't need to double the capacity.
'''


class Dequeue:
    def __init__(self):
        self.queue = []
        self.size = 10

    def insertFront(self, element):
        if len(self.queue) < self.size:
            self.queue.insert(0, element)
        else:
            print(-1)

    def insertRear(self, element):
        if len(self.queue) < self.size:
            self.queue.append(element)
        else:
            print(-1)

    def deleteFront(self):
        if len(self.queue) !=0 :
            self.queue.pop(0)
        else:
            print(-1)

    def deleteRear(self):
        if len(self.queue) !=0 :
            self.queue.pop()
        else:
            print(-1)

    def getFront(self):
        if self.queue:
            print(self.queue[0])
        else:
            print(-1)

    def getRear(self):
        if self.queue:
            print(self.queue[-1])
        else:
            print(-1)

            
deque = Dequeue()

flag = True
while flag:
    print('what you want to Do: ')
    print('''1. Insert at front    2.Insert at Rear    3.Delete at front
          4.Delete at rear    5. print front    6.print rear    7. exit''')
    
    choice = int(input())
    if choice == 1:
        data = int(input('enter the value: '))
        deque.insertFront(data)
    elif choice == 2:
        data = int(input('enter the value: '))
        deque.insertRear(data)
    elif choice == 3:
        deque.deleteFront()
    elif choice == 4:
        deque.deleteRear()
    elif choice == 5:
        deque.getFront()
    elif choice == 6:
        deque.getRear()
    elif choice == 7:
        flag = False
    else:
        print('Enter a valid Choice...')
