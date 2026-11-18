class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        x = 0

        for idx,i in enumerate(nums):
            need = target - i
            if need in seen:
                return [seen[need], idx]
            seen[i] = idx

        