class Node:
    def __init__(self):
        self.letters = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        tmp = self.root
        for c in word:
            tmp.letters[c] = tmp.letters.get(c, Node())
            tmp = tmp.letters[c]
        tmp.is_word = True

    def search(self, word: str) -> bool:
        def dfs(i: int, node: Node):
            if i == len(word):
                return node.is_word

            if word[i] == '.':
                for c in node.letters:
                    if dfs(i+1, node.letters[c]):
                        return True
            
            if word[i] in node.letters:
                return dfs(i+1, node.letters[word[i]])

            return False
        return dfs(0, self.root)