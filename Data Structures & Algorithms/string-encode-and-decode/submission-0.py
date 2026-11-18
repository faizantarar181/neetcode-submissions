class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        start = 0
        while start < len(s):
            hash_pos = start
            while s[hash_pos] != "#":
                hash_pos += 1
            length = int(s[start:hash_pos])
            word_start = hash_pos + 1
            result.append(s[word_start : word_start + length])
            start = word_start + length
        return result