class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        string=""
        cnt=32
        while(cnt):
            string+=str(n&1)
            n=n>>1
            cnt-=1
        return(int(string,2))
        