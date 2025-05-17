class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        reds, whites, blues = 0, 0, 0
        for i in nums:
            if i==0:
                reds += 1
            elif i ==1:
                whites += 1
            elif i == 2:
                blues += 1
        
        for i in range(reds):
            nums[i] = 0
        for i in range(reds, reds + whites):
            nums[i] = 1
        for i in range(reds + whites, reds + whites + blues):
            nums[i] = 2
