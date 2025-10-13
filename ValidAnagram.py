class ValidAnagram():
    def isAnagram(self, s, t):
        #Check length first
        if len(s) != len(t):
            return False
        #Turn strings into lists
        sChars = list(s)
        tChars = list(t)
        #Sort lists alphabetically
        sortedS = sorted(sChars)
        sortedT = sorted(tChars)
        #Compare lists
        for i in range(len(sortedS)):
            if(sortedS[i] != sortedT[i]):
                return False
        return True
    
testWord = "hellofhdsjd"
testCompare = "holelfhdsjd"
iA = ValidAnagram()
result = iA.isAnagram(testWord, testCompare)
print(result)