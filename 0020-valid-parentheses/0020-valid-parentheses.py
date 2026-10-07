class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for ch in s:
            if ch in "[{(":
                st.append(ch)
            else:
                if len(st)==0:
                    return False
                if ch==")":
                    elem=st.pop()
                    if elem!="(":
                        return False
                elif ch=="}":
                    elem=st.pop()
                    if elem!="{":
                        return False
                else:
                    elem=st.pop()
                    if elem!="[":
                        return False
        if len(st)==0:
            return True
        else:
            return False