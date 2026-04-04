class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st=[]
        for ch in logs :
            if ch == "../":
                if st :
                    st.pop()
            elif ch != "./" :
                st.append(ch)
        return len(st)
