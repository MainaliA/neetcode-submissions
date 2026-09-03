class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = dict()
        for words in strs:
            key = tuple(sorted(words))
            if key not in hashMap:
                hashMap[key] = []
            hashMap[key].append(words)
        return list(hashMap.values())