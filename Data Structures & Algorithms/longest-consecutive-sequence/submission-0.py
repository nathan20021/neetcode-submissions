class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq = set(nums)
        longestSequenceLength = 0
        for num in nums:
            currentSequenceLength = 1
            p = num
            while p + 1 in uniq:
                currentSequenceLength += 1
                p += 1
            longestSequenceLength = max(currentSequenceLength, longestSequenceLength)
        return longestSequenceLength
