class Solution:
    def maxProduct(self, nums):
        minending = nums[0]
        maxending = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            v1 = nums[i]
            v2 = minending * nums[i]
            v3 = maxending * nums[i]

            maxending = max(v1, v2, v3)
            minending = min(v1, v2, v3)

            res = max(res, maxending)

        return res