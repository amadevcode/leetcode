# Beginner Friendly Valid Parentheses Solution

# Disclaimer
#This is a simple stack-based solution. It works well as a base and can be simplified further.

# Approach
#Iterate through the string from left to right.
#
#If the current character is an opening bracket, push it onto the stack.
#
#If it is a closing bracket, check whether the stack is empty.
#
#If the stack is empty or the top element does not match, return False.
#
#After processing the whole string, the stack must be empty for the string to be valid.

# Complexity
# Time complexity:
#O(n)
# Space complexity:
#O(n)

# Solution Code
#
#
#python3
#
#1 <= s.length <= 104
#s consists of parentheses only '()[]{}'.
class Solution:
    def isValid(self, s: str) -> bool:
        openingCharacters = {
            "(" : 1,
            "{" : 2,
            "[" : 3,
        }

        closingCharacters = {
            ")" : 1,
            "}" : 2,
            "]" : 3,
        }

        string = list(s)

        charactersFound = []

        for i in range(0, len(string)):
            if string[i] in openingCharacters:
                c = openingCharacters[string[i]]
                charactersFound.append(c)
            elif string[i] in closingCharacters:
                c = closingCharacters[string[i]]
                if charactersFound != []:
                    if c == charactersFound[-1]:
                        charactersFound.pop(-1)
                    else:
                        return False
                else:
                    return False

        if charactersFound == []:
            return True
        else:
            return False
