from dll import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.history = DoublyLinkedList()
        self.node_store = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key not in self.node_store:
            return None
        else:
            node = self.node_store[key]

            self.history.move_to_front(node)
            return node.value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key not in self.node_store:
            self.history.add_to_head((key, value))
            self.node_store[key] = self.history.head


            if self.history.length > self.limit:
                del self.node_store[self.history.tail.value[0]]
                self.history.remove_from_tail()
            
        else:
            node = self.node_store[key]
            node.value = (key, value)
            self.history.move_to_front(node)

cache = LRUCache(3)
cache.set('item1', 'a')
cache.set('item2', 'b')
cache.set('item3', 'c')
print(cache.history)
# cache.set('item2', 'z')
# cache.get('item1')
# cache.get('item2')
# cache.set('item1', 'a')
# cache.set('item2', 'b')

# cache.set('item3', 'c')

# cache.get('item1')
# cache.set('item4', 'd')

# cache.get('item1')
# cache.get('item3')
# cache.get('item4')
# print(cache.history.head.next.next.value)
# cache.get('item2')


# a, z, c