class TwoSum:
    def twoSum(self, nums, target):
        numsToIndex = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numsToIndex:
                return [numsToIndex[complement], i]
            numsToIndex[num] = i