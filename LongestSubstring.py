class LongestSubstring():
    def lengthOfLongestSubstring(self, s):
        count = 0
        for i in range(len(s)):
            longestString = set()
            currentCount = 0
            for current in range(i,len(s)):
                if s[current] in longestString:
                    break
                longestString.add(s[current])
                currentCount += 1
                if currentCount > count:
                    count = currentCount
        return count
ls = LongestSubstring()
result = ls.lengthOfLongestSubstring("bbbdbafth")
print(result)