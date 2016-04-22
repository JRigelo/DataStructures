#linked list
import sys

class LinkedList():
  def __init__(self):
    self.head = None

  def prepend(self, value):
    node = Node()
    node.value = value
    previous = self.head
    node.next = previous
    self.head = node

  def size(self):
    if self.head == None:
      return 0

    n = self.head
    counter = 0
    while n:
      n = n.next
      counter += 1
    return counter

  def get(self, index):
    if index > self.size() - 1:
      raise ValueError('Index out of range')

    i = self.head
    counter = 0
    while i:
      if counter == index:
        return i.value
      i = i.next
      counter += 1

class Node(object):
  def __init__(self):
    self.value = None
    self.next = None

l = LinkedList()
l.prepend('Helena')
l.prepend('Joyce')
l.prepend('Callie')
l.prepend('Chris')

print "List is:\n"
for i in range(0, l.size()):
  print l.get(i),
