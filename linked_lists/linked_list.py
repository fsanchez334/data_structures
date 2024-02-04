import node as n

class LinkedList:
  def __init__(self, first_node):
    self.first_node = first_node

  def traverseList(self):
    current_node = self.first_node
    while current_node is not None:
        print(current_node.data)
        current_node = current_node.next
    
  def read_index(self, index):
    current_index = 0
    current_node = self.first_node
    while current_index < index:
      current_node = current_node.next
      current_index += 1
    return current_node.data

  def index_of(self, value):
    target_index = 0
    current_node = self.first_node
    while current_node.data != value:
      current_node = current_node.next
      target_index += 1
    return target_index

  def insert_value(self, index, value):
    current_index = 0
    current_node = self.first_node
    while current_index < index - 1:
      current_node = current_node.next
      current_index += 1
    #Now that we are here, we build out a Node
    new_node = n.Node(value)
    #We have the current node point to this new node - but we first must save it's original connecting neighbor
    old_neighbor = current_node.next
    current_node.next = new_node
    new_node.next = old_neighbor

  def delete_node(self, index):
    current_index = 0
    current_node = self.first_node
    if index == 0 and current_node.next is None:
      self.firt_node = current_node.next
      return
    elif index == 0 and current_node.next is not None:
      next_head = current_node.next
      current_node.next = None
      self.first_node = next_head
      return
    else:
      while current_index < index - 1:
        current_node = current_node.next
        current_index += 1
      new_neighbor = current_node.next.next
      current_node.next.next = None
      current_node.next = new_neighbor
  
  def reverseLinkedList(self):
    prev = None
    current = self.first_node
    next_node = current.next

    while current is not None:
      current.next = prev
      prev = current
      current = next_node
      if next_node is None:
        break
      else: 
        next_node= next_node.next
    
    self.first_node = prev
    