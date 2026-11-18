class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = []
        count = Counter(nums)
        
        count = sorted(count,key =count.get, reverse =True)
        
        
        for i in range(k):
            out.append(count[i])
        
        return out
                
        