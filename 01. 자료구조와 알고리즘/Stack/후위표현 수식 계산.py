class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    
    for token in tokenList:
        
        if type(token) == int:
            postfixList.append(token)
            
        else:
            if opStack.isEmpty():
                opStack.push(token)
                
            elif token == ')':
                while opStack.peek()!='(':
                    postfixList.append(opStack.pop())
                opStack.pop()
                
            elif prec[opStack.peek()] < prec[token] or token == "(":
                    opStack.push(token)
            else:
                while not opStack.isEmpty():
                    if prec[opStack.peek()] >= prec[token]:
                        postfixList.append(opStack.pop())
                    else:
                        break
                opStack.push(token)
                
    while not opStack.isEmpty():
        postfixList.append(opStack.pop())       

    return postfixList


def postfixEval(tokenList):
    opStack = ArrayStack()
    for token in tokenList:
        if type(token) == int:
            opStack.push(token)
        else:
            v1 = opStack.pop()
            v2 = opStack.pop()
            if token == '+':
                opStack.push(v2+v1)
            elif token == '-':
                opStack.push(v2-v1)
            elif token == '*':
                opStack.push(v2*v1)
            else:
                opStack.push(v2/v1)
    return opStack.pop()


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val
