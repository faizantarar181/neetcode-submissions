class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = (len(numbers) - 1)

        current = numbers[l] + numbers[r]

        
        while target != current:
            current = numbers[l] + numbers[r]
            if target < current:
                r -= 1
            if target > current:
                l += 1
        return [l + 1,r + 1]
        

        