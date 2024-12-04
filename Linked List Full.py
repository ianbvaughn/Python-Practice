class Node:
    def __init__(self,value,next_node=None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self,head=None):
        self.head=head
    def insert(self,value): #Insert new values into Linked List.
        node=Node(value) #Creates a new node using value passed into method.
        if self.head is None: #Checks to see if there are any other nodes in the Linked List.
            self.head = node #This node is now the head of the Linked List.
            return
        current=self.head #Find head of Linked List.
        while True:
            if current.next_node is None: #If we've reached the tail of the Linked List...
                current.next_node = node #Attach the new node to the tail.
                break
            current=current.next_node #Move onto the next node in the Linked List.
    def delete(self,value:int) -> Node:
        dummy = Node(0,self.head)
        prev,curr=dummy,self.head
        while curr:
            if curr.value == value:
                prev.next_node = curr.next_node
            else:
                prev=curr
            curr=curr.next_node
        return dummy.next_node
    def print(self):
        current=self.head
        while True:
            print(current.value, "->", end=" ")
            if current.next_node is None:
                print("None")
                break
            current=current.next_node

k = LinkedList()
k.insert(1) #'1' is now the head of Linked List 'k'.
k.insert(2)
k.insert(3)
k.insert(6)
k.print()
k.delete(2)
k.print()