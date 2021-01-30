class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []
        self.n = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            if node.n < 3:
                node.n += 1
                node.words.append(word)

    def find_word_by_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children: return ''
            node = node.children[c]
        return node.words


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        # products.sort()
        # cur = ""
        # res = []
        # for c in searchWord:
        #     cur+=c
        #     i = bisect.bisect_left(products,cur)
        #     word = [w for w in products[i:i+3] if w.startswith(cur)]
        #     res.append(word)
        # return res
        trie = Trie()
        products.sort()
        res, cur = [], ""
        for word in products:
            trie.addWord(word)
        for c in searchWord:
            cur += c
            res.append(trie.find_word_by_prefix(cur))
        return res