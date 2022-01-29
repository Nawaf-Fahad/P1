class Node:
 
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None
class DoubleLinkedList:
    def __init__(self):
       
        self.head = None
        self.tail = None
       
    def add(self,node):
        # for double linkied list
        # first case if data strc is empty
        if(self.head is None):
           
            self.head=node
            self.tail=self.head
        else: # second case if double linkied not empty
           
            self.tail.next = node
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        return self.tail
 
    def popItem(self):
        lastone = self.tail.key
       
        if self.tail == self.head:
           
            self.head = None
            self.tail = None
            return lastone
        self.tail.prev.next = None
        self.tail = self.tail.prev
        return lastone
 
       
       
       
       
class LRU_Cache(object):
 
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = {}
        self.dblist = DoubleLinkedList()
        pass
 
    def get(self, key):
        if key is None or key=="" or key not in self.dict:
            return "none"
       
        val = self.dict[key]
        self.dblist.add(Node(key=key, value=val))
        return val
       
        pass
 
    def set(self, key, value):
        if self.capacity <= 0:
            return "none"
        x=len(self.dict)
        if x == self.capacity:
           
            self.dblist.popItem()
 
        self.dict[key] = value
        pass

    
our_cache = LRU_Cache(5)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
 
our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache
 
our_cache.set(5, 5)
our_cache.set(6, 6)
our_cache1 = LRU_Cache(0) #none
our_cache2 = LRU_Cache(-1) #none

 