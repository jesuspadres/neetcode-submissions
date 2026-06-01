class Node:
        def __init__(self, val=None):
            self.val = val
            self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        curr = self.head
        for _ in range(index):
            if curr == None:
                return -1
            curr = curr.next
        return curr.val if curr else -1

    def insertHead(self, val: int) -> None:
        new = Node(val)
        new.next = self.head
        self.head = new
        if self.tail == None:
            self.tail = self.head

    def insertTail(self, val: int) -> None:
        if self.tail:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        else:
            self.tail = self.head = Node(val)

    def remove(self, index: int) -> bool:
        if index == 0:
            if self.head:
                if self.head == self.tail:
                    self.tail = None
                self.head = self.head.next
                return True
            return False

        prev = None
        curr = self.head
        for _ in range(index):
            if curr:
                prev = curr
                curr = curr.next
            else:
                return False
        if curr == self.tail:
            self.tail = prev
        if curr:
            prev.next = curr.next
            return True
        return False


    def getValues(self) -> List[int]:
        vals = []
        curr = self.head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        return vals
        
