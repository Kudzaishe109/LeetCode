class Solution:
    def removeDuplicates(self, s: str):#> str
        """
        #Understand
            I - str

            O - str

            C - 

            E - "" => ""
              - "cc" => ""
              - can I treat "A" the same as "a"
        #Plan
            initialize an empty stack
            loop through string:
                if the char on the top of the stack is the same as char[current]:
                    pop the element on the top of the stack
                else:
                    attend to the stack
            return all the charecters in the stack as a string

        #Implement
        """
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            elif char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
        