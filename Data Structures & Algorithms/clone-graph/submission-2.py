"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}
        visited = set()
        if not node:
            return None
        def dfs(node: Node):
            clones[node] = clone = clones.get(node, Node(node.val))
            if node in visited:
                return clone

            visited.add(node)
            for adj in node.neighbors:
                if clones.get(adj) not in clones[node].neighbors:
                    clones[node].neighbors.append(dfs(adj))

            visited.remove(node)
            return clones[node]
        return dfs(node)