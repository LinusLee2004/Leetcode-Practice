class MissingNumber():
    def missingNumber(self, nums):
        n = len(nums)
        testSet = set()
        for i in range(n + 1):
            testSet.add(i)
        for num in nums:
            if num in testSet:
                testSet.remove(num)
        return testSet.pop()
mn = MissingNumber()
arr = [0,2,3,4,1,6,7]
result = mn.missingNumber(arr)
print(result)