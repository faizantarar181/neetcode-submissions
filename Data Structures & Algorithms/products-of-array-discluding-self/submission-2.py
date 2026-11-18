class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = [1]
        right = [1] * len(nums)
        out = []

        for i in range(1,len(nums)):
            value = left[i - 1] * nums[i - 1]
            left.append(value)
        
       

        for j in range(len(nums) - 2,-1,-1):
            value = right[j + 1] * nums[j + 1]
            right[j] = value 
        
        for x in range(len(left)):
            value = left[x] * right[x]
            out.append(value)
        
        return out

        

