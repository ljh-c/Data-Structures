class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        # reference to next node
        self.next = next
    
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        # set this node's next reference to the node passed in
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_tail(self, value):
        new_node = Node(value)

        # if the linked list is empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            current_tail = self.tail
            current_tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        # if linked list is not empty
        elif self.head is self.tail:
            self.tail = None
        
        # return value at current head
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value
    
    def contains(self, query):
        current = self.head

        while current is not None:
            if current.get_value() == query:
                return True

            current = current.get_next()
        
        return False
    
    def get_max(self):
        current = self.head
        
        if current is None:
            return None
        elif current.get_next() == None:
            return current.get_value()

        max = current.get_value()

        while current is not None:
            if max < current.get_value():
                max = current.get_value()
            
            current = current.get_next()
        
        return max