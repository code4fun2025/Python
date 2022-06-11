class Trie(object):

    def __init__(self):
        self.children = defaultdict(Trie)
        self.isWord = False        

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.isWord = True       

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        cur = self
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
    
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
