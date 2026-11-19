class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for number in nums:
            if number in seen:
                return True
            seen[number] = True
        return False

