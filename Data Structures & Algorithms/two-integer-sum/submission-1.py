class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {}

        for i, n in enumerate(nums):
            num_index[nums[i]] = i
            
        for i, n in enumerate(nums):
            diff = target - n
            if diff in num_index and num_index[diff] != i:
                return [i, num_index[diff]]

        return []