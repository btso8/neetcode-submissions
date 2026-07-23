class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.nextnode = None

class MyHashSet:

    def __init__(self):
        self.hashset = []
        for _ in range(10**4):
            self.hashset.append(ListNode(0))

    def add(self, key: int) -> None:
        current = self.hashset[key % len(self.hashset)]
        while current.nextnode:
            if current.nextnode.key == key:
                return
            current = current.nextnode
        current.nextnode = ListNode(key)

    def remove(self, key: int) -> None:
        current = self.hashset[key % len(self.hashset)]
        while current.nextnode:
            if current.nextnode.key == key:
                current.nextnode = current.nextnode.nextnode
                return
            current = current.nextnode

    def contains(self, key: int) -> bool:
        current = self.hashset[key % len(self.hashset)]
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