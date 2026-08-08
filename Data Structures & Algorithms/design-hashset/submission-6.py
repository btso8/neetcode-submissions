class Node:
    
    def __init__(self, key):
        self.key = key
        self.next_node = None

class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.hashset = [Node(0) for _ in range(self.size)]

    def add(self, key: int) -> None:
        current = self.hashset[key % self.size]
        while current.next_node:
            if current.next_node.key == key:
                return
            current = current.next_node
        current.next_node = Node(key)

    def remove(self, key: int) -> None:
        current = self.hashset[key % self.size]
        while current.next_node:
            if current.next_node.key == key:
                current.next_node = current.next_node.next_node
                return
            current = current.next_node

    def contains(self, key: int) -> bool:
        current = self.hashset[key % self.size]
        while current.next_node:
            if current.next_node.key == key:
                return True
            current = current.next_node
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)