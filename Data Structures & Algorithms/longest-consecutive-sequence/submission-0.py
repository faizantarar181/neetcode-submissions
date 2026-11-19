class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count = sorted(nums)
        consistent = 1
        longest = 1

        for number in range(1, len(count)):
            if count[number] == count[number - 1]:
                continue
            if count[number] == count[number - 1] + 1:
                consistent += 1
            else:
                consistent = 1
            longest = max(longest, consistent)

        return longest