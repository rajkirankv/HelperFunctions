import data_structures


# return the substring between 2 given substrings
def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


# given a string, return the integer if the string represents an integer. Return 'none' otherwise
def strToInt(s):
    try:
        return int(s)
    except ValueError:
        return None


# def infix_to_postfix(s):
#     precedence = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3}
#
#     infix_list = s.split()
#     postfix_list = list()
#     stack = data_structures.Stack()
#
#     for c in infix_list:
#         if c in precedence:
#             # if c is an operator
#             if stack.is_empty() or precedence[stack.peek()] < precedence[c]:
#                 # push the operator if the stack is empty or if the operator is of higher precedence than
#                 # the most recent operator on the stack
#                 stack.push(c)
#             else:
#                 postfix_list.append(stack.pop())
#         elif c == ')':
#             # if c is a closed bracket, pop and append to the result until an opening bracket is met, and then pop
#             # that too. If the stack becomes empty, then exit the loop
#             while stack.peek() != '(':
#                 postfix_list.append(stack.pop())
#                 if stack.is_empty():
#                     break
#             # if the reason for exiting the loop is meeting the opening bracket, pop that bracket
#             if not stack.is_empty():
#                 stack.pop()
#         else:
#             # if c is neither an operator or a closed bracket, simply append it to the result list
#             postfix_list.append(c)
#
#     while not stack.is_empty():
#         postfix_list.append(stack.pop())
#
#     return ''.join(postfix_list)

# def infix_to_postfix(s):
#     precedence = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3}
#     s_list = s.split(sep = ' ')
#     postfix_list = list()
#     operator_stack = data_structures.Stack()
#
#     for c in s_list:
#         if c == '(':
#             operator_stack.push(c)
#         elif c in precedence:
#             if operator_stack.is_empty():
#                 operator_stack.push(c)
#             elif precedence[c] > precedence[operator_stack.peek()]:
#                 operator_stack.push(c)
#             else:
#                 top_operator = operator_stack.pop()  # Stack is not empty at this point. Neither is the top
#                 # operator of lower precedence than c
#                 while precedence[c] <= precedence[top_operator]:
#                     postfix_list.append(top_operator)
#                     operator_stack.pop()
#                     if operator_stack.is_empty():
#                         break
#                     else:
#                         top_operator = operator_stack.peek()
#                 operator_stack.push(c)  # The stack is either empty or has an operator with lower precedence at the top
#                 # In either case, push c, the operator in hand
#         elif c == ')':
#             top_operator = operator_stack.pop()
#             while top_operator != '(':
#                 postfix_list.append(top_operator)
#                 if operator_stack.is_empty():
#                     break
#                 else:
#                     top_operator = operator_stack.pop()  # This is either a '(' or an operator. Either way, pop
#         else:
#             postfix_list.append(c)
#
#     while not operator_stack.is_empty():
#         postfix_list.append(operator_stack.pop())
#
#     return ''.join(postfix_list)

def infix_to_postfix(s):
    precedence = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3}
    s_list = s.split(sep=' ')
    postfix_list = list()
    operator_stack = data_structures.Stack()

    for c in s_list:
        if c == '(':
            operator_stack.push(c)
        # operators
        elif c in precedence:
            if operator_stack.is_empty() or precedence[c] > precedence[operator_stack.peek()]:
                operator_stack.push(c)
            else:
                # top_operator =   # Stack is not empty at this point. Neither is the top
                # operator of lower precedence than c
                while not operator_stack.is_empty() and precedence[c] <= precedence[operator_stack.peek()]:
                    postfix_list.append(operator_stack.pop())
                operator_stack.push(c)  # The stack is either empty or has an operator with lower precedence at the top
                # In either case, push c, the operator in hand
        elif c == ')':
            while not operator_stack.is_empty() and operator_stack.peek() != '(' :
                postfix_list.append(operator_stack.pop())
        else:
            postfix_list.append(c)

    while not operator_stack.is_empty():
        postfix_list.append(operator_stack.pop())

    return ''.join(postfix_list)


# def postfix_evaluate(s):


# This function parses the expression string s to check for balanced brackets. Returns bool
def match(a, b):
    string_mapping = {'(': ')', '[': ']', '{': '}'}
    return string_mapping[a] == b


# check if an arithmetic expression has balanced parenthesis
def parse_expressions(s):
    stack = data_structures.Stack()
    for c in s:
        if c in "{[(":
            stack.push(c)
        elif c in ")]}":
            if not match(stack.pop(), c):
                return False  # Failure due to mismatch in the type of brackets used
        else:
            continue
    return stack.is_empty()
