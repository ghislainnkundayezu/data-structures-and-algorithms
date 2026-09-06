class CacheItem:
    def __init__(self, key=0, value=0, next_node=None, previous_node=None):
        self.key = key
        self.value = value
        self.next = next_node
        self.previous = previous_node
    
    def __repr__(self):
        next_item = self.next.key if self.next else None
        previous_item = self.previous.key if self.previous else None
        return f"[key: {self.key}, val: {self.value}, prev: {previous_item}, next: {next_item}]"

class LRUCache:
 
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_size = 0
        self.value_map = {}
        self.head = None
        self.tail = None 

    def get(self, key: int) -> int:
        # look for the item in the hashmap
        cache_node = self.value_map.get(key)

        if cache_node:
            self.__move_to_head(cache_node)

        # return the int value of found value or -1 if not found.
        return cache_node.value if cache_node else -1
        
        
    def put(self, key: int, value: int) -> None:
        cashe_node = self.value_map.get(key)
        # if the key exists move it to the head.
        if cashe_node:
            cashe_node.value = value
            self.__move_to_head(cashe_node)

        else: 
            # if the cache capacity is full remove the item at the tail.
            if (self.curr_size >= self.capacity) and self.tail:
                # if the tail exist and it points to a previous node.
                old_tail_key = self.tail.key
                self.value_map.pop(old_tail_key)
                if self.tail and self.tail.previous:
                    self.tail.previous.next = None
                    self.tail = self.tail.previous
                else:
                    self.tail = None
                    self.head = None
                
                self.curr_size -= 1

            # add the item at the head.
            new_cache_node = CacheItem(key, value)
            
            self.value_map[key] = new_cache_node
    
            if not self.head:
                self.head = new_cache_node
                self.tail = new_cache_node
            else:
                self.head.previous = new_cache_node
                new_cache_node.next = self.head
                self.head = new_cache_node
                
            
            # update the curr size of the list.
            self.curr_size += 1
            print("size: ", 1, " ", self)
    
    def __move_to_head(self, node) -> None:
        # if the head of the list is empty. 
        if not self.head:
            self.head = node
            self.tail = node

        # if the node exists and it's not the head
        if (node) and (node != self.head):
            # make the next pointer of the previous node point to the next pointer of the node.
            node.previous.next = node.next

            # if the node was a tail make it's previous element the new tail.
            if node == self.tail:
                self.tail = node.previous
            
            # if the node wasn't a tail.
            else:
                node.next.previous = node.previous
            
            # make the node a head.
            self.head.previous = node
            node.next = self.head
            node.previous = None
            self.head = node
    
    
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)