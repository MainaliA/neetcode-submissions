class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        numSet = set()
        for i in range(n):
            if nums[i] in numSet:
                return True
            else:
                numSet.add(nums[i])
                if len(numSet) > k:
                    numSet.remove(nums[i-k])
        return False