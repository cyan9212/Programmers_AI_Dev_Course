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

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    
    for s in S:
        if s.isalpha():
            answer+=s
        else:
            if opStack.isEmpty():
                opStack.push(s)
                
            elif s == ')':
                while opStack.peek()!='(':
                    answer+=opStack.pop()
                opStack.pop()
                
            elif prec[opStack.peek()] < prec[s] or s == "(":
                    opStack.push(s)
            else:
                while not opStack.isEmpty():
                    if prec[opStack.peek()] >= prec[s]:
                        answer += opStack.pop()
                    else:
                        break
                opStack.push(s)
                
    while not opStack.isEmpty():
        answer+=opStack.pop()  
    return answer
