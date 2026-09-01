class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       n = len(nums)
       nDict = dict()
       for i in range (n):
        if target - nums[i] in nDict:
            return [nDict[target - nums[i]], i]
        else:
            nDict[nums[i]] = i