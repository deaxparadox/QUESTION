import os
import sys

class Node:
    def __init__(self, index: int, parent: int, value: int) -> None:
        self.left: Node | None = None
        self.right: Node | None = None
        self.index = index
        self.parent = parent
        self.value = value

class BT:
    def __init__(self) -> None:
        self.root: None | Node = None
        
    def insert(self, index: int, parent: int, value: int) -> None:
        new_node: Node = Node(index, parent, value)
        if not self.root:
            self.root = new_node
        else:
            self._insert(self.root, new_node)
    def _insert(self, root: Node, new_node: Node) -> None:
        if new_node.parent < root.parent:
            if not root.left:
                root.left = new_node
            else:
                self._insert(root.left, new_node)
                
        else:
            if not root.right:
                root.right = new_node
            else:
                self._insert(root.right, new_node)
    
    left = 0
    right = 0
    left_file_sizes = []
    right_file_sizes = []
    absolute = 0 
    parent: list | None = None
    file_size: list | None = None 
    def preorder(self, temp: Node|None) -> None:
        if (temp):
            print(temp.parent, temp.index, temp.value)
            self.preorder(temp.left)
            self.preorder(temp.right)


def mostBalancedPartition(parent, files_size):
    print(parent, files_size)
    bt = BT()
    bt.parent = parent
    bt.file_size = files_size
    for i, p, f in zip(range(len(parent)),parent, files_size):
        bt.insert(i, p, f)
        
    mid = len(parent)//2
    bt.left, bt.right = parent[:mid], parent[mid:]
    bt.preorder(bt.root)
    print(bt.left_file_sizes, bt.right_file_sizes)

if __name__ == '__main__':

    # parent_count = int(input().strip())
    
    lines = sys.stdin.readlines()
    
    parent = []
    for n in map(int, lines[0].strip().split(" ")):
        parent.append(n)

    # for _ in range(parent_count):
    #     parent_item = int(input().strip())
    #     parent.append(parent_item)

    # files_size_count = int(input().strip())

    files_size = []
    for n in map(int, lines[1].strip().split(" ")):
        files_size.append(n)

    

    # for _ in range(files_size_count):
    #     files_size_item = int(input().strip())
    #     files_size.append(files_size_item)

    result = mostBalancedPartition(parent, files_size)

    print(result)