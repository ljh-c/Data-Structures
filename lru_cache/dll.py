class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
    
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = Node(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev
    
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

    def __str__(self):
        print_prev = "null" if self.prev is None else self.prev.value
        print_next = "null" if self.next is None else self.next.value
        return f"{self.value}. {print_prev} <- -> {print_next}! "
        # return "roodle"

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = Node
        self.length = 1 if node else 0
    
    def __len__(self):
        return self.length
    
    def add_to_head(self, value):
        if not self.head or not self.tail:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
        
        self.length += 1
    
    def move_to_front(self, node):
        # if node is self.head:
        #     return None

        # if self.tail is not node:    
        #     node.next.prev = node.prev
        
        # if self.tail is node:
        #     self.tail = self.tail.prev

        # if self.head:
        #     node.prev.next = node.next
        #     node.prev = None
        #     node.next = self.head
        #     self.head.prev = node
        #     self.head = node

        if node is self.head:
            return None
        # store a reference to the node we're going to move 
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(value)


    def remove_from_head(self):
        if not self.head or not self.tail:
            return None
        
        value = self.head.value
        self.delete(self.head)
        return value

    def remove_from_tail(self):
        if not self.head or not self.tail:
            return None
        
        old_tail = self.tail

        self.tail = self.tail.prev

        self.delete(old_tail)

        return old_tail.value

    def delete(self, node):
        if not self.head or not self.tail:
            return None

        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif self.head is node:
            self.head = node.next
            node.delete()
        elif self.tail is node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
        
        self.length -= 1
    
    def __iter__(self):
        item = self.head

        while item is not None:
            yield item.value
            item = item.next
    
    def __str__(self):
        return ", ".join([str(node) for node in self])
    
doubly_ll = DoublyLinkedList()
doubly_ll.add_to_head('a')
doubly_ll.add_to_head('b')
doubly_ll.add_to_head('c')
doubly_ll.move_to_front(doubly_ll.head.next)
