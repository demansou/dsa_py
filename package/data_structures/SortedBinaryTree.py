import math
from BinaryNode import BinaryNode
from BinaryTree import BinaryTree

class SortedBinaryTree(BinaryTree):
    def __init__(self):
        super(SortedBinaryTree, self).__init__()
    
    def __init__(self, node: BinaryNode):
        self._root = self._sort(node)
        self._size = self._size_subtree_recursive(self._root)
    
    def _sort(self, node: BinaryNode) -> BinaryNode:
        pass
    
    def _insert_iterative(self, node: BinaryNode, value: int) -> BinaryNode:
        if not node: return BinaryNode(value)
        current = node
        while current:
            if value < current.val:
                if not current.left:
                    current.left = BinaryNode(value)
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = BinaryNode(value)
                    break
                current = current.right
        return node
    
    def _insert_recursive(self, node: BinaryNode, value: int) -> BinaryNode:
        if not node: return BinaryNode(value)
        elif value < node.val: node.left = self._insert_recursive(node.left, value)
        else: node.right = self._insert_recursive(node.right, value)
        return node
    
    def _remove_iterative(self, node: BinaryNode, value: int) -> BinaryNode:
        if not node: return None
        current = node
        while current:
            if not current: continue
            elif value < current.val: current = current.left
            elif value > current.val: current = current.right
            else: # value == current.val
                if current.left and current.right:
                    current.val = self._max_iterative_dfs(current.left)
                    current.left = self._remove_iterative(current.left, current.val)
                elif not current.left:
                    current = current.right
                else: # not current.right
                    current = current.left
                break
        return node
    
    def _remove_recursive(self, node: BinaryNode, value: int) -> BinaryNode:
        if not node: return None
        elif value < node.val: node.left = self._remove_recursive(node.left, value)
        elif value > node.val: node.right = self._remove_recursive(node.right, value)
        else: # value == node.val
            if node.left and node.right:
                node.val = self._max_recursive(node.left)
                node = self._remove_recursive(node.left, node.val)
            elif not node.left:
                node = node.right
            else: # not node.right
                node = node.left
        return node
    
    def _find_iterative(self, node: BinaryNode, value: int) -> bool:
        current = node
        while current:
            if not current: continue
            elif value < current.val: current = current.left
            elif value > current.val: current = current.right
            else: return True
        return False
    
    def _find_recursive(self, node: BinaryNode, value: int) -> bool:
        if not node: return False
        elif value < node.value: return self._find_recursive(node.left, value)
        elif value > node.value: return self._find_recursive(node.right, value)
        else: return True
    
    def _min_iterative(self, node: BinaryNode) -> int:
        if not node: return math.inf
        current = node
        min_val = math.inf
        while current:
            if not current: continue
            min_val = min(current.val, min_val)
            current = current.left
        return min_val
    
    def _min_recursive(self, node: BinaryNode) -> int:
        if not node: return math.inf
        return min(node.val, self._min_recursive(node.left))
    
    def _max_iterative(self, node: BinaryNode) -> int:
        if not node: return -math.inf
        current = node
        max_val = -math.inf
        while current:
            if not current: continue
            max_val = min(current.val, max_val)
            current = current.right
        return max_val

    def _max_recursive(self, node: BinaryNode) -> int:
        if not node: return -math.inf
        return max(node.val, self._max_recursive(node.right))