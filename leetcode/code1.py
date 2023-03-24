# start 1
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_word = True
        
    def search(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_word
        
    def starts_with(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True
      
在上述代码中，我们定义了两个类：`TrieNode` 表示字典树节点，`Trie` 表示字典树数据结构。其中，`TrieNode` 类包含了一个字典 `children`，用于存储子节点，以及一个布尔值 `is_end_word`，表示当前节点是否为一个单词的结尾。

`Trie` 类包含了一个根节点 `root`，以及三个方法：

- `insert(word)`：向字典树中插入一个单词。
- `search(word)`：在字典树中查找一个单词，返回布尔值，表示是否找到。
- `starts_with(prefix)`：判断是否存在以某个前缀开头的单词。

这些方法的实现都是通过遍历字典树节点来实现的，其中 `insert` 方法会将单词中的每个字符都插入到字典树中，`search` 方法会在字典树中查找单词中的每个字符，如果找不到就返回 False，否则继续查找下一个字符，最后判断当前节点是否为单词结尾；`starts_with` 方法同理，只是在查找到前缀的最后一个字符时就返回 True，不需要判断当前节点是否为单词结尾。

这些方法的时间复杂度都是 O(m)，其中 m 表示单词的长度，因为需要遍历单词中的每个字符。而字典树的空间复杂度则取决于存储的单词数量和单词的长度，最坏情况下需要存储所有单词的所有字符，空间复杂度为 O(nm)，其中 n 表示单词的数量。
