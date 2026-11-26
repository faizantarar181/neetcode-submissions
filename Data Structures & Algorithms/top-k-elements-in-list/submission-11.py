class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]
        for number,freq in count.items():
            buckets[freq].append(number)
        
        out = []
        for freq in range(len(nums), 0, -1):
            for number in buckets[freq]:
                out.append(number)
                if len(out) == k:
                    return out

    