import time
start_time=time.time()
class Node(object):

	def __init__(self, data):
		self.data = data
		self.nextNode = None
		
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
		
    def insertEnd(self,data):
        self.size=self.size+1
        newNode=Node(data)
        
        actualNode=self.head
        
        if not self.head:
            self.head=newNode
        else:
            while actualNode.nextNode is not None:
                actualNode=actualNode.nextNode
            actualNode.nextNode=newNode


    def duplicate(self):
        newnode=None
        start=None
        currentNode=self.head
        if currentNode.nextNode is not None:
            next=currentNode.nextNode
            while next is not None:
                if currentNode.data ==  next.data and next.nextNode is None:
                    if newnode is None:
                        newnode=currentNode
                        start=newnode
                    else:
                        newnode.nextNode=currentNode
                        newnode=currentNode
                elif currentNode.data == next.data:
                    pass
                elif currentNode.data!=next.data:
                    if newnode is None:
                        newnode=currentNode
                        start=newnode
                    else:
                        newnode.nextNode=currentNode
                        newnode=currentNode
                if currentNode.data != next.data and next.nextNode is None:
                    newnode.nextNode=next
                    newnode=next
            
            
                currentNode=currentNode.nextNode
                next=next.nextNode
            
            
        else:
            start=currentNode
            newnode=currentNode
        newnode.nextNode=None    
    
        while start is not None:
            print("%d " % start.data,end=" ")
            start = start.nextNode



linkedlist=LinkedList()
linkedlist.insertEnd(10)
linkedlist.insertEnd(9)
linkedlist.insertEnd(9)
linkedlist.insertEnd(8)
linkedlist.insertEnd(8)
linkedlist.insertEnd(7)





linkedlist.duplicate()

print()
print(time.time()-start_time)
