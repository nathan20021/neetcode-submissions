class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1] * n
        suff = [1] * n
        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i-1]
        
        for j in range(1, n):
            i = n - 1 - j
            print(i)
            suff[i] = suff[i+1] * nums[i+1]
        return [i[0]*i[1] for i in zip(pref, suff)]