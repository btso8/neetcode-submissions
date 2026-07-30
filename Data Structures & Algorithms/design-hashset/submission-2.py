class ListNode:
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.length = 10000
        self.hashset = []
        for _ in range(self.length):
            self.hashset.append(ListNode(0))

    def add(self, key: int) -> None:
        current = self.hashset[key % self.length]
        while current.next:
            if current.next.key == key:
                return
            current = current.next
        current.next = ListNode(key)

    def remove(self, key: int) -> None:
        current = self.hashset[key % self.length]
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next

    def contains(self, key: int) -> bool:
        current = self.hashset[key % self.length]
        while current.next:
            if current.next.key == key:
                return True
            current = current.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)