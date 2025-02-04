class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sum = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i-1]<nums[i]:
                sum.append(sum[i-1]+nums[i])
            else:
                sum.append(nums[i])
        return max(sum)

