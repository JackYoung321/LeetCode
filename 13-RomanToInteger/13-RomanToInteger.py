class Solution:
    
   
    
    def romanToInt(self, s: str) -> int:
        
        Numerals = {'I' : 1,
               'V' : 5,
               'X' : 10,
               'L' : 50,
               'C' : 100,
               'D' : 500,
               'M' : 1000}
        
        value = 0 #Initialise the value which we will add our sum of numerals to
        
        for i in range(len(s)): #Looping through the indexes of the length of the string (1st index, 2nd index etc.)
            if i + 1 < len(s) and Numerals[s[i]] < Numerals[s[i+1]]: # If the next index value is less than the 
                                                                    #total string length, there is no more characters
                                                                    #after this. This also means there is no possibility
                                                            #for a subtraction operation e.g IV, XL as there are no 
                                                            #proceeding characters. 
                                                            
                                                            #Numerals[s[i]] searches for the letter in position i in the 
                                                        #string inside the Numerals table and embodies the respective
                                                    #value (e.g. Numerals[s[i]] where s[i] = V, = 5). If its smaller than 
                                                #the value of the proceeding character, it is a special case (like IV) so
                                                #we subtract, otherwise add the positive respective value of the char.
                value -= Numerals[s[i]]
            else:
                value += Numerals[s[i]]
            
        return value
