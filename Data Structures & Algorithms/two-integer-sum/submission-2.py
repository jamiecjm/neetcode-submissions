class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {} # O(n)

        for i, n in enumerate(nums): # O(n)
            diff = target - n
            if diff in num_index:
                return [num_index[diff], i]
            num_index[n] = i

        return []