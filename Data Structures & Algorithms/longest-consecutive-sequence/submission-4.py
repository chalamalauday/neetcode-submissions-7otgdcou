class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set(nums)
        long=0
        for n in nums:
            if n-1 not in st:
                curr=n
                stre=1
                while curr+1 in st:
                    stre+=1
                    curr+=1
                long=max(stre,long)
        return long
