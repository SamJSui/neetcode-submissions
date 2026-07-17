class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        """Standard recursive insert that handles root updates."""
        self.root = self._insert(self.root, key, val)

    def _insert(self, node: Node, key: int, val: int) -> Node:
        if not node:
            return Node(key, val)
        if key < node.key:
            node.left = self._insert(node.left, key, val)
        elif key > node.key:
            node.right = self._insert(node.right, key, val)
        else:
            node.val = val  # Update value if key already exists
        return node

    def get(self, key: int) -> int:
        """Iterative search is slightly more space-efficient (O(1) extra space)."""
        curr = self.root
        while curr:
            if key < curr.key: curr = curr.left
            elif key > curr.key: curr = curr.right
            else: return curr.val
        return -1

    def getMin(self) -> int:
        if not self.root: return -1
        return self._get_min_node(self.root).val

    def getMax(self) -> int:
        if not self.root: return -1
        curr = self.root
        while curr.right:
            curr = curr.right
        return curr.val

    def remove(self, key: int) -> None:
        self.root = self._remove(self.root, key)

    def _remove(self, node: Node, key: int) -> Node:
        if not node: return None

        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            # Case 1 & 2: 0 or 1 child
            if not node.left: return node.right
            if not node.right: return node.left
            
            # Case 3: 2 children. Find successor (smallest in right subtree)
            successor = self._get_min_node(node.right)
            node.key, node.val = successor.key, successor.val
            # Remove the successor node we just copied
            node.right = self._remove(node.right, successor.key)
            
        return node

    def _get_min_node(self, node: Node) -> Node:
        while node.left:
            node = node.left
        return node

    def getInorderKeys(self) -> List[int]:
        """Using a generator for a generalized, O(N) traversal."""
        def dfs(node):
            if node:
                yield from dfs(node.left)
                yield node.key
                yield from dfs(node.right)
        return list(dfs(self.root))