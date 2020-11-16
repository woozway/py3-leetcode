class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        T=O(n), S=O(1), Boyer-Moore algo
        """
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate
