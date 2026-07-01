import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for number in nums:

            arr=nums.copy()

            arr.remove(number)

            res.append(math.prod(arr))
        
        return res



