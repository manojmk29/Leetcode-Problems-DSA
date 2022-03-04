class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev, cnt, ans = None, 0, 0
        for i in range(1, len(nums)):
            diff = nums[i-1] - nums[i]
            if diff == prev:
                cnt += 1
                if(cnt>=3):
                    ans+=(cnt-2)
            else:
                cnt = 2
            prev = diff
        return(ans)