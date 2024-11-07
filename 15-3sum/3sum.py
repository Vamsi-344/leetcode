class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        jumped = {}

        res = []
        for i, num in enumerate(nums):
            counter = target - num
            if counter in jumped:
                res.append([counter, num])
            jumped[num] = i
        return res
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if list(set(nums))==[0]:
            return [[0,0,0]]
        res = []
        for i, num in enumerate(nums):
            counter = 0 - num
            inst_res = self.twoSum(nums[i+1:], counter)
            for i in inst_res:
                i.insert(0, num)
            res.extend(inst_res)
        resolve_res = [sorted(i) for i in res]
        return [list(i) for i in set(tuple(i) for i in resolve_res)]