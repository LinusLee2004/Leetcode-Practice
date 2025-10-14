class CountingBits():
    def countBits(self, n):
        ans = []
        for i in range(n + 1):
            onesCount = bin(i).count("1")
            ans.append(onesCount)
        return ans
            
cb = CountingBits()
result = cb.countBits(5)
print(result)