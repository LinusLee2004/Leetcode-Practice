class ClimbingStairs():
    def climbingStairs(self, n):
        if n <= 2:
            return n
        a,b = 1,2
        for _ in range(3, n + 1):
            temp = b
            b = a + b
            a = temp
        return b
        

x = ClimbingStairs.climbingStairs(ClimbingStairs, 3)
print(x)