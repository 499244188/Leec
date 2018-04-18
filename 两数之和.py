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