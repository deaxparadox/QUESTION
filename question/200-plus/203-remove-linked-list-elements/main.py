from typing import Any

class Node:
    def __init__(self, value) -> None:
        self.val = value
        self.next: Node | None = None
        
class LL:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.last: Node | None = self.head
        
    def insert(self, value: Any) -> None:
        if not self.head and not self.last:
            self.last = self.head  = Node(value)
            return
        else:
            self.last.next = Node(value)
            self.last = self.last.next
            return
    
    def print(self) -> None:
        temp: Node | None = self.head
        print("[", end="")
        while temp:
            t = temp            
            temp = temp.next
            if temp: print(t.val, end=",")
            else: print(t.val, end="")
        print("]")
  
    def remove_the_value(self, val: int):
        pre, move = self.head, self.head
        while move:
            if move.val == val and move == pre:
                t = self.head
                self.head = self.head.next
                pre, move = self.head, self.head
                del t
                continue
            
            if self.head is None:
                break
            
            if move.val == val:
                t = move
                if move.next is None:
                    move = pre
                    move.next = None
                    pre = move
                else:
                    move = pre
                    move = move.next.next
                    pre.next = move
                del t
            else:
                pre = move
                move = move.next


def main():
    l = LL()
    # target = 6
    # for i in [1,2,6,3,4,5,6]:
    #     l.insert(i)
    target = 7
    for i in [7, 7, 7, 7]:
        l.insert(i)
    
    # target = 1
    # for i in [1, 1, 1]:
    #     l.insert(i)
    l.remove_the_value(target)
    l.print()
            
if __name__ == "__main__":
    main()