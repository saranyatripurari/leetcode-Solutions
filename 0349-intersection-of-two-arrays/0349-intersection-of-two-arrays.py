class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:

        nums3 = []
        seen = set()

        # Store all unique elements of nums1
        for num in nums1:
            seen.add(num)

        # Check which elements of nums2 are also present in nums1
        for num in nums2:
            if num in seen and num not in nums3:
                nums3.append(num)

        return nums3