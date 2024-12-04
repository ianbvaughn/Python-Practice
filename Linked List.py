class Node:
    def __init__(self,value,next_node=None):
        self.value = value
        self.next_node = None
node1=Node(1)
node2=Node(2)
node3=Node(3)
node1.next_node=node2
node2.next_node=node3
current=node1
while True:
    print(current.value, "->", end=" ")
    if current.next_node is None:
        print("None")
        break
    else:
        current=current.next_node