'''
A balanced delimiter starts with an opening character ((, [, {), ends with a matching closing character (), ], } respectively), and has only other matching delimiters in between. A balanced delimiter may contain any number of balanced delimiters.

Examples
The following are examples of balanced delimiter strings:

()[]{}
([{}])
([]{})
The following are examples of invalid strings:
([)]
([]
[])
([})
Input is provided as a single string. Your output should be True or False according to whether the string is balanced. For example:

Input:
([{}])
Output:
True

'''

def is_balanced(delimiters):
    stack = []
    opening_delimiters = "([{"
    closing_delimiters = ")]}"
    delimiter_pairs = {"(": ")", "{": "}", "[": "]"}
    
    for delimiter in delimiters:
        if delimiter in opening_delimiters:
            stack.append(delimiter)
        elif delimiter in closing_delimiters:
            if not stack or delimiter_pairs[stack.pop()] != delimiter:
                return False
    
    return len(stack) == 0


input_string = "([{}])"
print(is_balanced(input_string)) 