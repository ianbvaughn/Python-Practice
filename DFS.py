# Create a binary tree.

class Node:
   def __init__(self,name,head=None):
      self.head = head #The head of this node is the one that we assign to it. If blank, there is no head.
      self.left = None
      self.right = None
      self.name = name
      self.children = []
      if self.head: #If this node has a head...
         if self.head.left is None: #If the head of this node has no left child...
            self.head.left = self #Assign this node as its left child.
            self.head.children.append(self)
         elif self.head.right is None: #If the head of this node has no right child...
            self.head.right = self #Assign this node as its right child.
            self.head.children.append(self)
         else: #If the head of this node has both a left and right child...
            raise OverflowError #Raise an exception.
   def __repr__(self):
      return self.name
   def get_children(self):
      return self.children #Return list of children.
n1 = Node("n1")
n2 = Node("n2",n1)
n3 = Node("n3",n1)
print(n1.get_children())