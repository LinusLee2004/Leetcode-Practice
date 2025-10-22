class LongestPalindromicSubstring():
    def workOutwards(self, s, left, right):
        while left >=0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]
    def longestPalindrome(self, s):
        longest = ""
        for i in range(len(s)):
            #Treats index like odd palindrome
            p1 = self.workOutwards(s, i, i)
            #Treats inedex as two centers for even palindrome
            p2 = self.workOutwards(s, i, i + 1)
            if len(p1) > len(longest):
                longest = p1
            if len(p2) > len(longest):
                longest = p2
        return longest

lps = LongestPalindromicSubstring()
print(lps.longestPalindrome("hannah aceca"))