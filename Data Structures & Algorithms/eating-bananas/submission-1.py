class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        hi=max(piles)
        res=max(piles)
        while l<=hi:
            k=(l+hi)//2
            toth=0
            for p in piles:
                toth+=math.ceil(float(p)/k)
            if toth <=h:
                res=k
                hi=k-1
            else:
                l=k+1
        return res
                
