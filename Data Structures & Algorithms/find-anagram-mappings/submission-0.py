class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cache = {}
        for i, num in enumerate(nums2):
            cache[num] = i

        for i, num in enumerate(nums1):
            nums1[i] = cache[num]

        return nums1