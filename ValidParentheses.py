#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
# Example 1:
#
# Input: s = "()"
#
# Output: true
#
# Example 2:
#
# Input: s = "()[]{}"
#
# Output: true
#
# Example 3:
#
# Input: s = "(]"
#
# Output: false
#
# Example 4:
#
# Input: s = "([])"
#
# Output: true
#
# Example 5:
#
# Input: s = "([)]"
#
# Output: false
class Solution:
    def isValid(self, s: str) -> bool:
        # the stack to keep track of opening brackets.
        stack = []

        # hash map for keeping track of mapping . This keeps the code very clean
        #Also makes adding more types of paranthesis easier
        mapping = {")" : "(", "}":"{", "]" : '['}
        # For every bracket in the expression
        for char in s:

            #If the character is an closing bracket
            if char in mapping:

                #pop the top most element from the stack , if it is non empty
                # otherwise assign a dummy value of '# to the top element variable
                top_element = stack.pop() if stack else "#"

                # the mapping for the opening bracket in our hash and the top
                # element of stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # we have an opening bracket, simply push it onto the stack
                stack.append(char)
        return not stack