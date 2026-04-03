class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ev=[]
        od=[]
        for i in nums:
            if i %2==0:
                ev.append(i)
            else:
                od.append(i)
        return ev+od
        