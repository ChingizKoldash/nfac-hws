from typing import List, Any, Dict, Set, Generator

class StaticArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None] * capacity

    def set(self, index: int, value: int) -> None:
        if index < 0 or index >= self.capacity:
            raise IndexError
        self.array[index] = value

    def get(self, index: int) -> int:
        if index < 0 or index >= self.capacity:
            raise IndexError
        return self.array[index]

class DynamicArray:
    def __init__(self):
        self.array = []

    def append(self, value: int) -> None:
        self.array.append(value)

    def insert(self, index: int, value: int) -> None:
        if index > len(self.array):
            raise IndexError
        self.array.insert(index, value)

    def delete(self, index: int) -> None:
        if index >= len(self.array):
            raise IndexError
        del self.array[index]

    def get(self, index: int) -> int:
        if index >= len(self.array):
            raise IndexError
        del self.array[index]

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value: int) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:  
            current = current.next
        current.next = new_node

    def insert(self, position: int, value: int) -> None:
        if position < 0:
            raise IndexError
        
        new_node = Node(value)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        for _ in range(position - 1):
            if current is None: 
                raise IndexError
            current = current.next
        
        new_node.next = current.next
        current.next = new_node

    def delete(self, value: int) -> None:
        current = self.head
        if current and current.value == value:
            self.head = current.next
            return
        
        prev = None
        while current and current.value != value:
            prev = current
            current = current.next
        
        if current is None:  
            raise ValueError
        
        prev.next = current.next

    def find(self, value: int) -> Node:
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def size(self) -> int:
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self) -> bool:
        return self.head is None

    def print_list(self) -> None:
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
    
    def reverse(self) -> None:
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def get_head(self) -> Node:
        return self.head
    
    def get_tail(self) -> Node:
        current = self.head
        while current and current.next:
            current = current.next
        return current

class DoubleNode:
    def __init__(self, value: int, next_node = None, prev_node = None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value: int) -> None:
        new_node = DoubleNode(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert(self, position: int, value: int) -> None:
        if position < 0:
            raise IndexError()
        
        new_node = DoubleNode(value)

        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if not self.tail:
                self.tail = new_node
            return
        
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError()
            current = current.next
        
        if current is None:
            raise IndexError()

        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current

        if new_node.next is None:
            self.tail = new_node

    def delete(self, value: int) -> None:
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                return
            current = current.next
        raise ValueError()

    def find(self, value: int) -> DoubleNode:
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def size(self) -> int:
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self) -> bool:
        return self.head is None

    def print_list(self) -> None:
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    def reverse(self) -> None:
        current = self.head
        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev
        
        self.head, self.tail = self.tail, self.head

    def get_head(self) -> DoubleNode:
        return self.head

    def get_tail(self) -> DoubleNode:
        return self.tail
class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        def _insert(node, value):
            if not node:
                return TreeNode(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node
        
        self.root = _insert(self.root, value)

    def delete(self, value: int) -> None:
        def _delete(node, value):
            if not node:
                return node
            if value < node.value:
                node.left = _delete(node.left, value)
            elif value > node.value:
                node.right = _delete(node.right, value)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                min_node = self._min_value_node(node.right)
                node.value = min_node.value
                node.right = _delete(node.right, min_node.value)
            return node
        
        self.root = _delete(self.root, value)

    def search(self, value: int) -> Optional[TreeNode]:
        def _search(node, value):
            if not node or node.value == value:
                return node
            if value < node.value:
                return _search(node.left, value)
            return _search(node.right, value)

        return _search(self.root, value)

    def inorder_traversal(self) -> List[int]:
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)

        _inorder(self.root)
        return result
    
    def size(self) -> int:
        def _size(node):
            if not node:
                return 0
            return 1 + _size(node.left) + _size(node.right)

        return _size(self.root)

    def is_empty(self) -> bool:
        return self.root is None

    def height(self) -> int:
        def _height(node):
            if not node:
                return -1
            left_height = _height(node.left)
            right_height = _height(node.right)
            return 1 + max(left_height, right_height)

        return _height(self.root)

    def preorder_traversal(self) -> List[int]:
        result = []
        def _preorder(node):
            if node:
                result.append(node.value)
                _preorder(node.left)
                _preorder(node.right)

        _preorder(self.root)
        return result

    def postorder_traversal(self) -> List[int]:
        result = []
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                result.append(node.value)

        _postorder(self.root)
        return result

    def level_order_traversal(self) -> List[int]:
        if not self.root:
            return []
        result = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)  # Pop the first element from the list
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def minimum(self) -> Optional[TreeNode]:
        def _min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current
        
        return _min_value_node(self.root) if self.root else None

    def maximum(self) -> Optional[TreeNode]:
        def _max_value_node(node):
            current = node
            while current.right:
                current = current.right
            return current

        return _max_value_node(self.root) if self.root else None

    def is_valid_bst(self) -> bool:
        def _is_valid_bst(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            if node.value <= low or node.value >= high:
                return False
            return _is_valid_bst(node.left, low, node.value) and _is_valid_bst(node.right, node.value, high)
        
        return _is_valid_bst(self.root)

def insertion_sort(lst: List[int]) -> List[int]:
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def selection_sort(lst: List[int]) -> List[int]:
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

def bubble_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

def shell_sort(lst: List[int]) -> List[int]:
    n = len(lst)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2
    return lst

def merge_sort(lst: List[int]) -> List[int]:
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1
    return lst

def quick_sort(lst: List[int]) -> List[int]:
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
