class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max = 0
        
        for i in range(0,len(nums)):
            if i > max:
                return 0
            max = max if(i+nums[i]<max)else(i+nums[i])
        return 1
            