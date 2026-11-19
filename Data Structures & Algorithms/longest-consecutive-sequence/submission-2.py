class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0

        for number in numbers:
            if (number - 1) not in numbers:
                consistent = 1
                while (number + 1) in numbers:
                    consistent += 1
                    number += 1
                longest = max(longest, consistent)

        return longest