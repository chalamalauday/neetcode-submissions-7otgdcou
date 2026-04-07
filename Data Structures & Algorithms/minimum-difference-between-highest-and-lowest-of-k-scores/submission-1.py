class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        ans=float('inf')
        for r in range(len(nums)):
            if r-l+1>k:
                l+=1
            if r-l+1==k:
                ans=min(ans,nums[r]-nums[l])
        return ans
        