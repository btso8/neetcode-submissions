class Node:

    def __init__(self, key: int):
        self.key = key
        self.nextnode = None

class MyHashSet:

    def __init__(self):
        self.size = 100
        self.hashset = []
        for _ in range(self.size):
            self.hashset.append(Node(-1))

    def hasher(self, key: int) -> int:
        return self.hashset[key % self.size]

    def add(self, key: int) -> None:
        current = self.hasher(key)
        while current.nextnode:
            if current.nextnode.key == key:
                return
            current = current.nextnode
        current.nextnode = Node(key)

    def remove(self, key: int) -> None:
        current = self.hasher(key)
        while current.nextnode:
            if current.nextnode.key == key:
                current.nextnode = current.nextnode.nextnode
                return
            current = current.nextnode

    def contains(self, key: int) -> bool:
        current = self.hasher(key)
        while current.nextnode:
            if current.nextnode.key == key:
                return True
            current = current.nextnode
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)