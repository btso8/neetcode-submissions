class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.nextnode = None

class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.hashmap = []
        for _ in range(self.size):
            self.hashmap.append(Node(-1, -1))

    def put(self, key: int, value: int) -> None:
        current = self.hashmap[key % self.size]
        while current.nextnode:
            if current.nextnode.key == key:
                current.nextnode.value = value
                return
            current = current.nextnode
        current.nextnode = Node(key, value)

    def get(self, key: int) -> int:
        current = self.hashmap[key % self.size]
        while current.nextnode:
            if current.nextnode.key == key:
                return current.nextnode.value
            current = current.nextnode
        return -1

    def remove(self, key: int) -> None:
        current = self.hashmap[key % self.size]
        while current.nextnode:
            if current.nextnode.key == key:
                current.nextnode = current.nextnode.nextnode
                return
            current = current.nextnode

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)