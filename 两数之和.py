'''
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


        a1 = 0
        li = []
        for i in nums:
            a1+=1
            b1 = 0
            for j in nums[nums.index(i)+1:]:
                b1+=1
                if(target==i+j):
                    li.append(a1-1)
                    li.append(a1+b1-1)
                    return li