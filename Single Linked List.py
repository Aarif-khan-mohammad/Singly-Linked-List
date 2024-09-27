class Node: #Creating Node

    def __init__(self , item = None , next = None):
        self.item = item
        self.next = next

class SLL:

    def __init__(self , start=None): #start is partial node which contains None , when we create new node then,we give reference of first node
        self.start = start

    def is_empty(self): #checking weather the list is empty or not
        return self.start == None
    
    def insert_at_start(self , data):
        n = Node(data , self.start) #creating a new node which contains data/value and refernce to the next item
        self.start = n #we need give refernce of the first node to the start node

    def insert_at_last(self , data):
        n = Node(data) #not giving sencond parameter , due to last node , we need not give refernce , last node refernce is None

        if not self.is_empty(): #cheching the list is empty or not , if it is not empty
            temp = self.start #temp is storing the refernce of starting node in the start 
            while temp.next is not None: #iterates untill the last node which contains , the refernce is None
                temp = temp.next#to continue to the next node 
            temp.next = n # now assigning , refernce of new node at the last node refernce which is initally None
        else: # if list is empty then we need to assign the new node at the start/starting node
            self.start = n

    def search(self , data):
        temp = self.start
        while temp is not None:#loop runs untill last node
            if temp.item == data:
                return temp
            temp = temp.next#to continue to the next node 
        return None #if the data is not found it returns None
    
    def insert_after(self , temp , data): #passing reffernce of the node in temp
        if temp is not None:
            n = Node(data , temp.next)# final value's refernce is assigning to new node
            temp.next = n #new node referce is assigning to the before element 
        
    
    def delete_first(self):
        self.start = self.start.next # refering the 2nd node from the start , which means we are skipping the first node

    def delete_last(self):
        if self.start is None: #if list empty , leave it
            pass
        elif self.start.next is None: # if list had one node , which has its refrence in start, so we need to remove it
            self.start = None #so we need to make the start refernce to the None, which makes is it empty
        else: # if it contains more than 2 nodes
            temp= self.start
            while temp.next.next is not None:#we need to reach before the node of last node
                temp = temp.next
            temp.next = None # if it reach 2nd last node which make it none , which means thier is no refernce before last node
        
    def delete_item(self , data):
        if self.start is None:
            pass
        elif self.start.next is None:#if one node exist
            if self.start.item == data:
                self.start = None
        else:
            temp = self.start
            if temp.item == data:#if the first node is the node we are deleting then, give the refernce of 2nd node in start
                self.start = temp.next
            else:
                while temp.next is not None:# runs untill last node
                    if temp.next.item == data: #if temp(1st) node's next is 2nd node's item is matched data than
                        temp.next= temp.next.next # assign the 4th node's refernce , in the 2nd node, which skiping the 3rd node
                        break
                    temp = temp.next


    def print_list(self):
        temp = self.start#temp is storing the refernce of starting node in the start 
        while temp is not None:#iterates untill the last node which contains , the refernce is None
            print(temp.item , end=" ")
            temp = temp.next #it contiune to next node
    
    def __iter__(self):
        return SLLIterator(self.start)

class SLLIterator: #without this class we can't use loops against our list
    def __init__(self ,start):
        self.current = start #current is similar to temp
    
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration #raising an exception to stop iteration , if their is not items
        data = self.current.item
        self.current = self.current.next
        return data

mylist = SLL()
mylist.insert_at_start(20) #20
mylist.insert_at_start(80) #80 20
mylist.insert_at_last(54) #80 20 54
mylist.insert_at_start(90) #90 80 20 54
mylist.insert_at_start(50) #50 90 80 20 54
mylist.insert_at_last(14) #50 90 80 20 54 14
mylist.insert_after(mylist.search(20) , 45) #50 90 80 20 45 54 14
mylist.delete_first() #90 80 20 45 54 14
mylist.delete_last() #90 80 20 45 54
mylist.delete_item(45) #90 80 20 54
mylist.print_list()
for x in mylist:
    print(x)#90 80 20 54
