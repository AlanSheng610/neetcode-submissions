class PrefixTree:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        cur = self
        
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = PrefixTree()
            
            cur = cur.children[ch]
        cur.is_end = True


    def search(self, word: str) -> bool:
        cur = self

        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]

        return True if cur.is_end == True else False
        

    def startsWith(self, prefix: str) -> bool:
        cur = self

        for ch in prefix:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        
        return True 
        
        
        