class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            k="".join(sorted(i))
            if k not in d:
                d[k]=[]
            d[k].append(i)
        # for m in strs:
        #     a="".join(sorted(m))
        #     if a in d:
        #         d[a].append(m)
        v=d.values()
        return list(v)
            
        