class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=Counter(nums)
        ma=max(d.values())
        for i in nums:
            if d[i]==ma:
                return i