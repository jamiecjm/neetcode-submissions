class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        previous = None
        for current in nums:
            if previous == current:
                return True
            previous = current
        return False

