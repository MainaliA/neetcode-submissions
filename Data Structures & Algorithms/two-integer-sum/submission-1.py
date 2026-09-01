class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nDict = dict()
        for i in range (n):
            if target - nums[i] not in nDict:
                nDict[nums[i]] = i
            else:
                return [nDict[target - nums[i]], i]
