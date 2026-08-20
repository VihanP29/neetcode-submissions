class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0]*n
        suff = [0]*n
        res = [0]*n
        pref[0] = 1
        suff[n-1] = 1
        count = 1
        for i in range(1, n):
            count = nums[i-1] * count
            pref[i] = count
        count = 1
        for i in range(n-2, -1, -1):
            count = nums[i+1] * count
            suff[i] = count
        for i in range(n):
            res[i] = pref[i]*suff[i]
        return res