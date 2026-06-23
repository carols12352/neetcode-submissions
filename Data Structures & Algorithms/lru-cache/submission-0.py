class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.dic = {}
        self.capa = capacity

        self.head = ListNode()
        self.tail = ListNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def move_to_head(self, node):
        self.remove(node)
        self.add_to_head(node)

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1

        node = self.dic[key]
        self.move_to_head(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.move_to_head(node)
            return

        node = ListNode(key, value)
        self.dic[key] = node
        self.add_to_head(node)

        if len(self.dic) > self.capa:
            old = self.tail.prev
            self.remove(old)
            del self.dic[old.key]