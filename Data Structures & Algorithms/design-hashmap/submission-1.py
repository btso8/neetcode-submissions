class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.hashmap = []
        for _ in range(self.size):
            self.hashmap.append(Node(0,0))
        
    def hasher(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        current = self.hashmap[self.hasher(key)]
        while current.next:
            if current.next.key == key:
                current.next.value = value
                return
            current = current.next
        current.next = Node(key, value)

    def get(self, key: int) -> int:
        current = self.hashmap[self.hasher(key)]
        while current.next:
            if current.next.key == key:
                return current.next.value
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        current = self.hashmap[self.hasher(key)]
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)