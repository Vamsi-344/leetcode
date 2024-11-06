class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        jumped = {}

        for i, num in enumerate(nums):
            counter = target - num

            if counter in jumped:
                return [jumped[counter], i]
            
            jumped[num] = i
        
        