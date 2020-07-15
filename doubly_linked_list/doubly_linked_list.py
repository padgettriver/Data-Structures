
"""
Each ListNode holds a reference to its previous node
as well as its next node in the List. 
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def __del__(self):
        self.value = None
     
        if (self.next == None) and (self.prev == None):
            pass
        elif (self.next) and (self.prev == None):
                self.next.prev = None
                self.next = None
        elif (self.prev) and (self.next == None):
            self.prev.next = None
            self.prev = None
        else:
            self.prev.next = self.next
            self.next.prev = self.prev
            self.prev = None
            self.next = None
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        lNode = ListNode(value)
        self.length += 1
        if self.length == 1:
            self.head = lNode
            self.tail = lNode
        else:
            lNode.next = self.head
            self.head.prev = lNode
            self.head = lNode
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        curVal = self.head.value
        self.length -= 1
        if self.head.next != None:
            self.head = self.head.next
            self.__del__()
        else:
            self.head.__del__()
            self.head = None
            self.tail = None
        return curVal
        pass
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        lNode = ListNode(value)
        self.length += 1
        if self.length == 1:
            self.head = lNode
            self.tail = lNode
        else:
            lNode.prev = self.tail
            self.tail.next = lNode
            self.tail = lNode
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        curVal = self.tail.value
        self.length -= 1
        if self.tail.prev != None:
            self.tail = self.tail.prev
            self.__del__()
        else:
            self.tail.__del__()
            self.head = None
            self.tail = None
        #return the value
        return curVal
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):

        if self.head.next is not None and node is not self.head:
            if node is self.tail:
                self.tail = self.tail.prev
            self.length -= 1
            self.add_to_head(node.value)
            node.__del__()
        else:
            pass

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):

        if self.head.next is not None and node is not self.tail:
            if node is self.head:
                self.head = self.head.next
            self.add_to_tail(node.value)
            node.__del__()
            self.length -= 1  
        else:
            pass


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            if node is self.head:
                self.head = node.next
            elif node is self.tail:
                self.tail = node.prev

            node.__del__()
            

        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self): 
        current = self.head.next
        max_val = self.head.value
        while current is not None:
            if current.value > max_val:
                max_val = current.value
            current = current.next

        return max_val 