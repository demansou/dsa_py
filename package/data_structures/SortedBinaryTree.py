from BinaryNode import BinaryNode
from BinaryTree import BinaryTree

class SortedBinaryTree(BinaryTree):
    def __init__(self):
        super().__init__()
    
    def __insert_iterative(self, node: BinaryNode, value: int) -> BinaryNode:
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
    
    def __insert_recursive(self, node: BinaryNode, value: int) -> BinaryNode:
        if not node: return BinaryNode(value)
        elif value < node.val: node.left = self.__insert_recursive(node.left, value)
        else: node.right = self.__insert_recursive(node.right, value)
        return node
    
    def __remove_iterative(self, node: BinaryNode, value: int) -> BinaryNode:
        if not node: return None
        current = node
        while current:
            if not current: continue
            elif value < current.val: current = current.left
            elif value > current.val: current = current.right
            else: # value == current.val
                if current.left and current.right:
                    current.val = self.__max_iterative_dfs(current.left)
                    current.left = self.__remove_iterative(current.left, current.val)
                elif not current.left:
                    current = current.right
                else: # not current.right
                    current = current.left
                break
        return node
    
    def __remove_recursive(self, node: BinaryNode, value: int) -> BinaryNode:
        if not node: return None
        elif value < node.val: node.left = self.__remove_recursive(node.left, value)
        elif value > node.val: node.right = self.__remove_recursive(node.right, value)
        else: # value == node.val
            if node.left and node.right:
                node.val = self.__max_recursive(node.left)
                node = self.__remove_recursive(node.left, node.val)
            elif not node.left:
                node = node.right
            else: # not node.right
                node = node.left
        return node
    
    def __find_iterative(self, node: BinaryNode, value: int) -> bool:
        current = node
        while current:
            if not current: continue
            elif value < current.val: current = current.left
            elif value > current.val: current = current.right
            else: return True
        return False
    
    def __find_recursive(self, node: BinaryNode, value: int) -> bool:
        if not node: return False
        elif value < node.value: return self.__find_recursive(node.left, value)
        elif value > node.value: return self.__find_recursive(node.right, value)
        else: return True