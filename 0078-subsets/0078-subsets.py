class Solution:
    def subsets(self, nums):
        ans = []

        def rec(i, temp):
            if i == len(nums):
                ans.append(temp.copy())
                return

            # Don't take
            rec(i + 1, temp)

            # Take
            temp.append(nums[i])
            rec(i + 1, temp)

            temp.pop()

        rec(0, [])

        return ans