class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mi=(l+r)//2
            if(nums[mi]==target):
                return mi
            elif(nums[mi]>target):
                r=mi-1
            else:
                l=mi+1
        return -1
        