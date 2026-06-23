class ListNode:
    def __init__(self, key=0, val=0, next=None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.head = ListNode()
        self.tail = ListNode()

        self.tail.prev = self.head
        self.head.next = self.tail

        self.capa = capacity
        self.dic = {}

    def remove(self, node: ListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_front(self, node:ListNode):
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node 
    
    def add_to_head(self, node: ListNode):
        self.remove(node)
        self.move_front(node)

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        
        node = self.dic[key]
        self.add_to_head(node)

        return node.val

        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.add_to_head(node)
            return
        
        node = ListNode(key, value)
        self.dic[key] = node
        self.move_front(node)

        if len(self.dic) > self.capa:
            old = self.tail.prev
            self.remove(old)
            del self.dic[old.key]


