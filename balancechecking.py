"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #12 - Braces Brackets & Bows Balance (balancechecking.py)


Author: Ali Qattan

Difficulty Level: 6/10

Prompt: In your IDEs, your code editors and sometimes Vim (for those 
unfortunate ones who use vim) your application will yell at you when you don’t
have matching closing brackets. Python does not have that problem as much as
other languages like Java and C which rely heavily on curly braces.  You need 
to write a program that allows for that functionality so that every ‘[‘ and ‘{‘ 
and ‘(‘ has a matching ‘]’  ‘}’  ‘)’. 
This problem can be solved quickly using the right data structure.

Test Cases:
Input: {[()]}  Output: True

Input: [()]  Output: True

Input:{[{}]  Output: False

"""
class Solution:
    def s_case(char):
         if char == "[" or "]":
            return("Bracket")
         if char == "(" or ")":
            return("Parenthesis")
         if char == "{" or "}":
            return("C-Bracket")
    def isBalanced(self, parenthesis): 
            #type parenthesis: string
            #return type: boolean
            def s_case(char):
                if char == "[" or "]":
                    return("Bracket")
                if char == "(" or ")":
                    return("Parenthesis")
                if char == "{" or "}":
                    return("C-Bracket")
            
            new = [i for i in parenthesis]     
            if len(new)%2 == 1:
                return False
            for i in range(int(len(new)/2)):
                if s_case(new[i]) != s_case(new[(-1*i)-1]):
                    return False
            return True

def main():
    str1=input()
    tc1= Solution()
    ans=tc1.isBalanced(str1)
    print(ans)

if __name__ == "__main__":
    main()