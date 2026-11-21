class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for idx,number in enumerate(numbers):
            need = target - number
            if need in seen:
                return[seen[need] + 1, idx + 1]
            seen[number] = idx
        

        