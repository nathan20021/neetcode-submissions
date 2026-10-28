class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i, num in enumerate(nums):
            complement[target - num] = i
        for i, num in enumerate(nums):
            if num in complement and complement[num] != i:
                return [i, complement[num]]
        