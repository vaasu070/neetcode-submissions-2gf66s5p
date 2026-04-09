
class Node:
    def __init__(self, key, val):
            self.key, self.val = key, val
            self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap  = capacity
        self.cache  ={}
        self.lru = Node(0 , 0 )
        self.mru = Node(0  , 0)

        self.lru.next = self.mru
        self.mru.prev  =  self.lru
    
    def remove(self , Node):

        # remove from the stack
        
        prev_node = Node.prev
        next_node = Node.next

        prev_node.next = next_node
        next_node.prev  =prev_node
    def insert(self , Node):
        # insert right before mru
        right_node = self.mru.prev
        self.mru.prev = Node
        right_node.next = Node
        Node.next = self.mru
        Node.prev = right_node



    
    def get(self, key: int) -> int:

        if key in self.cache:
            # update the stack
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val
        
        return - 1
    

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
           
       
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache)>self.cap:
                lru = self.lru.next
                self.remove(lru)
                del self.cache[lru.key]
        




        
