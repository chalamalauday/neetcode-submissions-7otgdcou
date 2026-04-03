class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        pref=[0]*len(nums)
        suff=[0]*len(nums)
        pref[0]=1
        suff[len(nums)-1]=1
        for i in range(1,len(nums)):
            pref[i]=pref[i-1]*nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            suff[j]=suff[j+1]*nums[j+1]
        for i in range(len(nums)):
            res[i]=pref[i]*suff[i]
        return res