class ContainsDuplicate():
    def containsDuplicate(self, nums):
        hash = set()
        for i, num in enumerate(nums):
            if num in hash:
                return True
            else:
                hash.add(num)
        return False