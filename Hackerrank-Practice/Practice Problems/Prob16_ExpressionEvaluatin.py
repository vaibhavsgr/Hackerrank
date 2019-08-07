"""
1. While there are still tokens to be read in,
   1.1 Get the next token.
   1.2 If the token is:
       1.2.1 A number: push it onto the value stack.
       1.2.2 A variable: get its value, and push onto the value stack.
       1.2.3 A left parenthesis: push it onto the operator stack.
       1.2.4 A right parenthesis:
         1 While the thing on top of the operator stack is not a
           left parenthesis,
             1 Pop the operator from the operator stack.
             2 Pop the value stack twice, getting two operands.
             3 Apply the operator to the operands, in the correct order.
             4 Push the result onto the value stack.
         2 Pop the left parenthesis from the operator stack, and discard it.
       1.2.5 An operator (call it thisOp):
         1 While the operator stack is not empty, and the top thing on the
           operator stack has the same or greater precedence as thisOp,
           1 Pop the operator from the operator stack.
           2 Pop the value stack twice, getting two operands.
           3 Apply the operator to the operands, in the correct order.
           4 Push the result onto the value stack.
         2 Push thisOp onto the operator stack.
2. While the operator stack is not empty,
    1 Pop the operator from the operator stack.
    2 Pop the value stack twice, getting two operands.
    3 Apply the operator to the operands, in the correct order.
    4 Push the result onto the value stack.
3. At this point the operator stack should be empty, and the value
   stack should have only one value in it, which is the final result."""


def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def computeExpression(a, b, op):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        return a/b


def parseExpression(e):
    values = []
    operators = []

    i = 0

    while i < len(e):

        if e[i] == " ":
            i += 1
            continue

        elif e[i] == "(":
            operators.append(e[i])

        elif e[i].isdigit():
            val = 0
            values.append(e[i])
            while (i < len(e) and e[i].isdigit()):
                val = (val * 10) + int(e[i])
                i += 1

        elif e[i] == ")":
            while len(operators) != 0 and operators[-1] != "(":
                b = values.pop()
                a = values.pop()
                op = operators.pop()
                result = computeExpression(a, b, op)
                values.append(result)

            operators.pop()

        elif len(operators)!=0 and precedence(e[-1]) >= precedence(e[i]):
            b = values.pop()
            a = values.pop()
            op = operators.pop()
            values.append(computeExpression(a, b, op))

            operators.append(token)
        i += 1

    while len(operators) != 0:
        b = values.pop()
        a = values.pop()
        op = operators.pop()
        values.append(computeExpression(a, b, op))

    print (values[-1])


if __name__ == "__main__":

    print(parseExpression("10 + 2 * 6"))
    print(parseExpression("100 * 2 + 12"))
    print(parseExpression("100 * ( 2 + 12 )"))
    print(parseExpression("100 * ( 2 + 12 ) / 14"))
