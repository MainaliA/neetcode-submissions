class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range (n):
            for j in range (n):
                if i != j and target - nums[i] == nums[j]:
                    return([i,j])
        