# start 1
class Node:
    children = {}
    isWord = False

class StreamChecker(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.word = ""
        self.root = Node()
        for word in words:
            node = self.root
            word = word[::-1]
            for w in word:
                if w not in node.children:
                    node.children[w] = Node()
                node = node.children[w]
            node.isWord = True
            del node
    
    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.word = letter + self.word 
        word = self.word
        if len(word)==0:
            return False
        
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
            if node.isWord:
                return True
        return False
    
st = StreamChecker(["cd","f","kl"])
# ["a"],["b"],["c"],["d"],["e"],["f"],["g"],["h"],["i"],["j"],["k"],["l"]
print("query a:",st.query("a"),st.word)
print("query b:",st.query("b"),st.word)
print("query c:",st.query("c"),st.word)
print("query d:",st.query("d"),st.word)
print("query e:",st.query("e"),st.word)
print("query f:",st.query("f"),st.word)
print("query g:",st.query("g"),st.word)
print("query h:",st.query("h"),st.word)
print("query i:",st.query("i"),st.word)
print("query j:",st.query("j"),st.word)
print("query k:",st.query("k"),st.word)
print("query l:",st.query("l"),st.word)