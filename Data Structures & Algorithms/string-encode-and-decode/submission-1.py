class Solution:

    def encode(self, strs: List[str]) -> str:
        sen = ""
        for i in strs:
            length = str(len(i)) + "#"
            sen += length + i
        return sen




    def decode(self, s: str) -> List[str]:
        out = []
        start = 0

        while start < len(s):
            hash_pos = start
            while s[hash_pos] != "#":
                hash_pos += 1
            length = int(s[start:hash_pos])
            word_start = hash_pos + 1
            word = s[word_start:word_start + length]
            out.append(word)
            start = word_start + length
        
        return out
                    


