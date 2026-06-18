class Solution:
    def maxProduct(self, nums):

        curr_max = nums[0]
        curr_min = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):

            num = nums[i]

            temp_max = curr_max

            curr_max = max(
                num,
                num * curr_max,
                num * curr_min
            )

            curr_min = min(
                num,
                num * temp_max,
                num * curr_min
            )

            result = max(result, curr_max)

        return result