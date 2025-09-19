class TwoSum:
    def twoSum(self, nums, target):
        numsToIndex = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numsToIndex:
                return [numsToIndex[complement], i]
            numsToIndex[num] = i

if __name__ == "__main__":
    solution = TwoSum() 

    nums = [11,18,2,7]

    target = 9

    result = solution.twoSum(nums, target)

    print(result)