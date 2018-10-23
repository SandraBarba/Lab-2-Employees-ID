#Student: Sandra Barba
#UTEP ID: 80641786
#Professor: Diego Aguire


class node:
   
    def __init__(self, data=-1):
        self.data = data
        self.next = None
        
class linked_list:
    #Constructor of the linked list
    def __init__(self):
        self.head = None #Give an empty list
    
    #Method to add an item to the linked list    
    def append(self, data):
        #Create a new node with the data given
        new_node = node(data)
        #If the list is empty, set node as new head
        if self.head==None:
            self.head=new_node
        else:
            cur = self.head
            #Traverse list until final item of the linked list
            while cur.next != None:
                cur = cur.next
            #Add new node
            cur.next = new_node
    
    #Method do print elements in the linked list
    def display(self):
        elems = [] #Empty list
        cur_node = self.head #
        #While the actual element in the list is not empty
        while cur_node != None:
            #Add element to the list
            elems.append(cur_node.data)
            #Go to next element
            cur_node = cur_node.next
        #Print all elements in the list
        print (elems)
        
    #Method to compare all elements in the linked list to check if there are
    #repeated elements
    def solution1(self):
        temp = self.head #Declare temporary pointer of the list
        counter = 0 #Declare counter to know position of the element
        #While the actual element in the list is not empty
        while(temp != None):
            counter2 = 0 #Declare a second counter
            cur = self.head #Declare a second temporary pointer of the list
            while(cur != None):
                #If the first and second pointer of the list are the same
                # and they are not in the same position then, they are repeated
                if(temp.data == cur.data and counter != counter2):
                    print("Number ", cur.data, " is repeated")
                cur = cur.next #Go to next node
                counter2 +=1 #Increment position of the second pointer
            temp = temp.next #Go to next node
            counter +=1 #Increment position of the first pointer
        
    #Method to apply bubble sort to the linked list
    def bubbleSort(self):
        swapped = True
        while swapped:
            swapped = False
            prev = self.head
            cur = self.head.next
            while cur != None:
                if prev.data < cur.data:
                    temp = prev.data
                    prev.data = cur.data
                    cur.data = temp
                    swapped = True    
                cur = cur.next #Go to next node with second pointer
                prev = prev.next #Go to next node with first pointer
    
    
  #this function will take the linked list and merged it.          
def mergeList(l1, l2):
    temp = None
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.data <= l2.data:
        temp = l1
        temp.next = mergeList(l1.next, l2)
    else:
        temp = l2
        temp.next = mergeList(l1, l2.next)
    return temp
#This function will sort the linked list using mergeList and division.
def mergeSort(head):
    if head is None or head.next is None:
        return head
    l1, l2 = divideList(head)
    l1 = mergeSort(l1)
    l2 = mergeSort(l2)
    head = mergeList(l1, l2)
    return head
#this function is used in the merge sort to divide de linked list in equal parts. 
def divideList(head):
    slow = head
    fast = head
    if fast:
        fast = fast.next
    while fast:
        fast = fast.next
        if fast:
            fast = fast.next
            slow = slow.next
    mid = slow.next
    slow.next = None
    return head, mid            
        
    

    
activision = open("activision.txt")
vivendi = open("vivendi.txt")

activision_file = activision.readlines()
vivendi_file = vivendi.readlines()
my_list = linked_list()
for ln in activision_file:
    ln = int(ln)
    my_list.append(ln)
for ln2 in vivendi_file:
    ln2 = int(ln2)
    my_list.append(ln2)

          
#my_list.display()


#my_list.bubbleSort() 
#my_list.solution1()

my_list.head = mergeSort(my_list.head)
my_list.display() 
        
            