import re


def add_char(str):
    str += ';'
    return str


def tokenze(code: str) -> list:
    return code.split()


def op_prior(char_op: str):
    if char_op == "^":
        return 6
    elif char_op == "*":
        return 5
    elif char_op == "/":
        return 5
    elif char_op == "%":
        return 3
    elif char_op == "+":
        return 2
    elif char_op == "-":
        return 2


def isOp(c: str) -> bool:
    if c == "-" or c == "+" or c == "*" or c == "/" or c == "^":
        return True
    return False


def opn(code: str) -> None:
    p = 0
    op_stack: list = []
    res: list = []
    while True:
        v = code[p]
        p += 1
        if v == ';':
            break
        if re.match("[0-9]+[.]*[0-9]*", v) or re.match("[A-Za-z]+", v):
            res.append(v)
        elif isOp(v):
            while (len(op_stack) > 0 and
                   op_stack[-1] != "(" and
                   op_prior(v) <= op_prior(op_stack[-1])):
                res.append(op_stack.pop())
              
            op_stack.append(v)
        elif v == ')':
            while len(op_stack) > 0:
                x = op_stack.pop()
                if x == '(':
                    break
                res.append(x)
        elif v == "(":
            op_stack.append(v)
    while len(op_stack) > 0:
        res.append(op_stack.pop())

    return res


def valid_string(string_input):
    string_input = add_char(string_input)
    str_correct = ''
    Pol_not_str = ''
    for c in string_input:
        if c == "-" or c == "+" or c == "*" or c == "/" or c == "^" or c == "(" or c == ")":
            str_correct += ' ' + c + ' '
        elif (c == ";"):
            str_correct += ' ' + c
        else:
            str_correct += c
    Pol_not_list = opn(tokenze(str_correct))
    for element in Pol_not_list:
        Pol_not_str += str(element)+' '
    return Pol_not_str
