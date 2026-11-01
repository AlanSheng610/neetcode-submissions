class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encode_strs = ""
        for i, n in enumerate(strs):
            # print(str(len(n)))
            encode_strs += chr(len(n)) + '#' + n
        return encode_strs
    def decode(self, s: str) -> List[str]:
        res = []
        print(s)
        i = 0
        while i < len(s):
            n = ord(s[i])
            res.append(str(s[i+2:i+2+n]))
            i += 2 + n
        return res
        
            
