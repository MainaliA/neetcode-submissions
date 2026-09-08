class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = dict()
        for i in range (n):
            if nums[i] not in freq:
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1
        sortedfreq = sorted(freq.items(), reverse = True, key = lambda x: x[1] )
        kfreq = sortedfreq[0:k]
        ans = [x[0] for x in kfreq]
        return list(ans)
        
        