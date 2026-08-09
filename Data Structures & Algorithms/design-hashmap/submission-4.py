class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_node = None

class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.hashmap = [Node(0, 0) for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        current = self.hashmap[key % self.size]
        while current.next_node:
            if current.next_node.key == key:
                current.next_node.value = value
                return
            current = current.next_node
        current.next_node = Node(key, value)

    def get(self, key: int) -> int:
        current = self.hashmap[key % self.size]
        while current.next_node:
            if current.next_node.key == key:
                return current.next_node.value
            current = current.next_node
        return -1

    def remove(self, key: int) -> None:
        current = self.hashmap[key % self.size]
        while current.next_node:
            if current.next_node.key == key:
                current.next_node = current.next_node.next_node
                return
            current = current.next_node

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)