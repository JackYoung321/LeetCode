class Solution:
    def isHappy(self, n: int) -> bool:

        previousIteration = []
        
        while n != 1:
            stringOfN = n
            n = 0
            for v in str(stringOfN):
                n += int(v) ** 2
            
            if n in previousIteration:
                return False
            else:
                previousIteration.append(n)
            
            
        return True # Broken out of the while loop indicating n has reached the value of 1 (n == 1)
                
            
