import math
from BinaryNode import BinaryNode

class BinaryTree:
    def __init__(self):
        super().__init__()
        self._root = None
        self._size = 0
    
    def __init__(self, node: BinaryNode):
        super().__init__()
        self._root = node
        self._size = self._size_subtree_recursive(self._root)
    
    def size(self) -> int:
        return self._size
    
    def insert(self, value: int) -> bool:
        if self.find(value): return False
        self._root = self._insert_recursive(self._root, value)
        self._size += 1
        return True
    
    def remove(self, value: int) -> bool:
        if not self.find(value): return False
        self._root = self._remove_recursive(self._root, value)
        self._size -= 1
        return True
    
    def find(self, value: int) -> bool:
        return self._find_recursive(self._root, value)
    
    def last_value(self) -> int:
        return self._last_value_recursive(self._root)
    
    def sum(self) -> int:
        return self._sum_recursive(self._root)
    
    def min(self) -> int:
        return self._min_recursive(self._root)
    
    def max(self) -> int:
        return self._max_recursive(self._root)
    
    def _insert_iterative(self, node: BinaryNode, value: int) -> BinaryNode:
        if not node: return BinaryNode(value)
        queue = [node]
        while queue:
            current = queue.pop(0)
            if not current.left:
                current.left = BinaryNode(value)
                break
            if not current.right:
                current.right = BinaryNode(value)
                break
            queue.append(current.left)
            queue.append(current.right)
        
        return node
    
    def _insert_recursive(self, node: BinaryNode, value: int) -> BinaryNode:
        if not node: return BinaryNode(value)
        elif self._size_subtree_recursive(node.left) <= self._size_subtree_recursive(node.right):
            node.left = self._insert_recursive(node.left, value)
        else: node.right = self._insert_recursive(node.right, value)
        return node
    
    def _remove_iterative(self, node: BinaryNode, value: int) -> BinaryNode:
        if not node: return None
        queue = [node]
        while queue:
            current = queue.pop(0)
            if not current: continue
            if value == current.val:
                if current.left and current.right:
                    last_value = self._last_value_iterative(current.right)
                    current.right = self._remove_iterative(current.right, last_value)
                    current.val = last_value
                    pass
                elif not current.left:
                    current = current.right
                else: # not current.right
                    current = current.left
            queue.append(current.left)
            queue.append(current.right)
        return node

    def _remove_recursive(self, node: BinaryNode, value: int) -> BinaryNode:
        if not node: return None
        if value == node.val:
            if node.left and node.right:
                last_value = self._last_value_recursive(node.right)
                node.right = self._remove_recursive(node.right, last_value)
                node.val = last_value
            elif not node.left: return node.right
            else: # not node.right
                return node.left
        else:
            node.left = self._remove_recursive(node.left, value)
            node.right = self._remove_recursive(node.right, value)
        return node

    
    def _find_bfs(self, node: BinaryNode, value: int) -> bool:
        if not node: return False
        queue = [node]
        while queue:
            current = queue.pop(0)
            if not current: continue
            if value == current.value: return True
            queue.append(current.left)
            queue.append(current.right)
        return False
    
    def _find_dfs(self, node: BinaryNode, value: int) -> bool:
        if not node: return False
        stack = [node]
        while stack:
            current = stack.pop()
            if not current: continue
            if value == current.value: return True
            stack.append(current.left)
            stack.append(current.right)
        return False
    
    def _find_recursive(self, node: BinaryNode, value: int) -> bool:
        if not node: return False
        if value == node.value: return True
        return self._find_recursive(node.left, value) or self._find_recursive(node.right, value)
    
    def _last_value_iterative(self, node: BinaryNode) -> int:
        last_value = None
        queue = [node]
        while queue:
            current = queue.pop(0)
            if not current: continue
            last_value = current.val
            queue.append(current.left)
            queue.append(current.right)
        return last_value
    
    def _last_value_recursive(self, node: BinaryNode) -> int:
        if not node: return None
        if last_val_right:= self._last_value_recursive(node.right): return last_val_right
        if last_val_left := self._last_value_recursive(node.left): return last_val_left
        return node.val
    
    def _sum_iterative_bfs(self, node: BinaryNode) -> int:
        if not node: return 0
        queue = [node]
        sum = 0
        while queue:
            current = queue.pop(0)
            if not current: continue
            sum += current.val
            queue.append(current.left)
            queue.append(current.right)
        return sum
    
    def _sum_iterative_dfs(self, node: BinaryNode) -> int:
        if not node: return 0
        stack = [node]
        sum = 0
        while stack:
            current = stack.pop()
            if not current: continue
            sum += current.val
            stack.append(current.left)
            stack.append(current.right)
        return sum
    
    def _sum_recursive(self, node: BinaryNode) -> int:
        if not node: return 0
        return node.val + self._sum_recursive(node.left) + self._sum_recursive(node.right)
    
    def _min_iterative_bfs(self, node: BinaryNode) -> int:
        if not node: return -math.inf
        queue = [node]
        min_val = math.inf
        while queue:
            current = queue.pop(0)
            if not current: continue
            min_val = min(current.val, min_val)
            queue.append(current.left)
            queue.append(current.right)
        return min_val
    
    def _min_iterative_dfs(self, node: BinaryNode) -> int:
        if not node: return -math.inf
        stack = [node]
        min_val = math.inf
        while stack:
            current = stack.pop()
            if not current: continue
            min_val = min(current.val, min_val)
            stack.append(current.left)
            stack.append(current.right)
        return min_val
    
    def _min_recursive(self, node: BinaryNode) -> int:
        if not node: return math.inf
        return min(node.val, self._min_recursive(node.left), self._min_recursive(node.right))
    
    def _max_iterative_bfs(self, node: BinaryNode) -> int:
        if not node: return math.inf
        queue = [node]
        max_val = -math.inf
        while queue:
            current = queue.pop(0)
            if not current: continue
            max_val = min(current.val, max_val)
            queue.append(current.left)
            queue.append(current.right)
        return max_val
    
    def _max_iterative_dfs(self, node: BinaryNode) -> int:
        if not node: return math.inf
        stack = [node]
        max_val = -math.inf
        while stack:
            current = stack.pop()
            if not current: continue
            max_val = max(current.val, max_val)
            stack.append(current.left)
            stack.append(current.right)
        return max_val
    
    def _max_recursive(self, node: BinaryNode) -> int:
        if not node: return -math.inf
        return max(node.val, self._max_recursive(node.left), self._max_recursive(node.right))
    
    def _size_subtree_iterative_bfs(self, node: BinaryNode) -> int:
        if not node: return 0
        queue = [node]
        size = 0
        while queue:
            current = queue.pop(0)
            if not current: continue
            size += 1
            queue.append(current.left)
            queue.append(current.right)
        return size
    
    def _size_subtree_iterative_dfs(self, node: BinaryNode) -> int:
        if not node: return 0
        stack = [node]
        size = 0
        while stack:
            current = stack.pop()
            if not current: continue
            size += 1
            stack.append(current.left)
            stack.append(current.right)
        return size
    
    def _size_subtree_recursive(self, node: BinaryNode) -> int:
        if not node: return 0
        return 1 + self._size_subtree_recursive(node.left) + self._size_subtree_recursive(node.right)
