class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = Counter(s)
        list_t = Counter(t)

        if list_s == list_t:
            return True
        else:
            return False

        