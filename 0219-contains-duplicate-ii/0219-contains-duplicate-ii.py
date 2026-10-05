class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        seen = {}

        for i in range(len(nums)):

            # If number is already present
            if nums[i] in seen:

                # Check distance between current index
                # and previous index
                if i - seen[nums[i]] <= k:
                    return True

            # Store/update the latest index of this number
            seen[nums[i]] = i

        return False