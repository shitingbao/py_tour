class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.insert(word)

    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word

    def starts_with(self, prefix):
        current_node = self.root
        words = []
        for char in prefix:
            if char not in current_node.children:
                return []
            current_node = current_node.children[char]
        self._dfs(current_node, prefix, words)
        return words

    def _dfs(self, node, prefix, words):
        if node.is_end_of_word:
            words.append(prefix)
        for char in node.children:
            self._dfs(node.children[char], prefix + char, words)

t = Trie(["cd","f","kl"])

for (k,v) in t.root.children.items():
    print("key:",k)