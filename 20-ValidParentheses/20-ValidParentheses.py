class Solution:
    def isValid(self, s: str) -> bool:
       
        characters = {'(' : ')',
                    '{' : '}',
                     '[' : ']'
                    }
        
        T = False # Set initial truth checking value to false
        last_char = s[-1] # Get the last value in the sample string to know when to finish checking
        for a in s: # For each character in the string
           
            for i, v in characters.items():  # For i (key), v (value) in the character dictionary
              
                if T == True: # If the truth checking value has been set to true from checking the previous character
                    
                    if a != tempVal:    #If the next character in the sequence does NOT match the corresponding value 
                                        #this is done by setting tempVal to v at the time of matching a to the key value                                         #in the below else statement
                                
                        return False    #If the truth checking statement was triggered and the corresponding match wasn't 
                                        #found, return false
                    
                    else:               # There is a match (closing bracket has been found)
                        
                        if a != last_char:  # If the closed bracket isn't the final character in the string
                            T = False       # Set the truth checking value back to false
                            break           # Break out of the current for loop to check the next string character
                            
                        else:               # If it is the last character
                            return True     #The string has been fully checked, with all open brackets being closed
                        
                        
                else:               #If the truth value is not set to True (we arent expecting a bracket to close)

                    if a == i:      #If the current character matches one of the keys in the dictionary

                        tempVal = v  # Set the tempVal to the value corresponding to the respective key (as this has
                                     #been set as the corresponding closing bracket)
                        T = True     #Set truth checking statement to true
                        break        #Break out the for loop to check the next letter
                    
                    #else:
                        #return False # Contains a character that is not accepted - This would be added if the current
                        #constraints did not exist
                       
#TESTED VALUES:
#"()"
#"()[]"
#"()[}"
#"()[]{}"
#"(]"

#EXPECTED OUTPUTS:
#TRUE
#TRUE
#FALSE
#TRUE
#FALSE
                    

        
        
        
        
        
        
        
   
                    
                
