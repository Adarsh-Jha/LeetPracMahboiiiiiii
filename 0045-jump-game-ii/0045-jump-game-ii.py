class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = len(nums) - 1
        jumps = 0
        
        while target != 0:
            for i in range(0,target):
                if i+nums[i] >= target:
                    target = i
                    break
            jumps+=1
        
        return jumps
        