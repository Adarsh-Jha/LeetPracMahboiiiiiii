class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        lb = 0 #left border
        rb = n - 1 #right border
        i = 0
        while i <= rb:
            if nums[i] == 2:
                nums[rb],nums[i] = nums[i],nums[rb]
                rb-=1
            elif nums[i] == 1:
                i+=1
            else:
                nums[lb],nums[i] = nums[i],nums[lb]
                lb+=1
                i+=1
        return nums

