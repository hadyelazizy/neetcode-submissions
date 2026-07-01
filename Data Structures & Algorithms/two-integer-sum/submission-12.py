class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_={}

        for index,num in enumerate(nums):

            hash_[num]=index
        
        for index,num in enumerate(nums):

            diff=target-nums[index]

            if diff in hash_ and hash_[diff] != index:
                return sorted([index,hash_[diff]])

