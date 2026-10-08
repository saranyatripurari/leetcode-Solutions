class Solution:
    def twoSum(self, nums, target):
        d={}
        for i in range(len(nums)):
            elem=nums[i]
            pe=target-elem
            if pe not in d:
                d[elem]=i
            else:
                return [d[pe],i]