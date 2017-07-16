# Uses python3
"""
Task: Your friend is maing text editor for programmers. He is currently working on a
feature that will find errors in the usage of different types of brackets. Code can
contain any brackets from the set []{}().
For convenience the text editor should not only inform the user that there is an error
in the usage of brackets, but also point to the exact place in the code with the
problematic code. First priority is to find the first unmatched closing bracket. If there
are no such mistakes then it should find the first unmatched opening bracket. If there
are not mistakes, text editor should inform the user that the usage of brackets is correct.

Apart from the brackets, code can contain bid and small latin letters, digits and
punctuation marks.

Input: Input contains one string S which consists of big and small latin letters,
digits, punctuation marks and brackets from the set of []{}()

Constraints: The length of S is at least 1 and at most 10^5.

Output format: If the code in S users brackets correctly, output "Success". Otherwise
output the 1-based index of the first unmatched closing bracket, and if there are no
unmatched closing brackets output the 1-based index of the first unmatched opening
bracket.
"""

def check_brackets(code):
    stack = []
    opening_brackets = frozenset(['[', '(', '{'])
    closing_brackets = frozenset([']', ')', '}'])
    for index, char in enumerate(code):
        if char in opening_brackets:
            stack.append((index + 1, char))
        elif char in closing_brackets:
            _, open_bracket = stack[-1] if stack else (None, None)
            if ((open_bracket == '[' and char == ']') or
                    (open_bracket == '{' and char == '}') or
                    (open_bracket == '(' and char == ')')):
                stack.pop()
            else:
                return index + 1
    return "Success" if len(stack) == 0 else stack[-1][0]



c = input()
print(check_brackets(c))