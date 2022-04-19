class Solution:
    def defangIPaddr(self, address: str) -> str:
        ret=""
        for i in address:
            if i==".":
                ret+="[.]"
            else:
                ret+=i
        return(ret)
        
        