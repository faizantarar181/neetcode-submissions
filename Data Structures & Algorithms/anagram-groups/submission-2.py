class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for i in strs:
            word = "".join(sorted(i))
            if word in groups:
                groups[word].append(i)
            else:
                groups[word] = []
                groups[word].append(i)

        
        return list(groups.values())
    

