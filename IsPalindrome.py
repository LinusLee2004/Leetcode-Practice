class IsPalindrome():
    def isPalindrome(self, s):
        clean = "".join(ch for ch in s if ch.isalnum())
        cleaned = clean.upper()
        for i in range(len(cleaned) // 2):
            if cleaned[i] != cleaned[len(cleaned) - 1 - i]:
                return False
        return True
        
                
test = "racecare"
test2 = "hellolleh"
test3 = "r(ace:c'ar"

ip = IsPalindrome()

result = ip.isPalindrome(test)
result2 = ip.isPalindrome(test2)
result3 = ip.isPalindrome(test3)

print(result)
print(result2)
print(result3)