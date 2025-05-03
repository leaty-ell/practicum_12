def calculate(s):
    def evaluate(tokens):
        stack = []
        num = 0
        sign = '+'
        while tokens:
            token = tokens.pop(0)
            if token.isdigit():
                num = num * 10 + int(token)
            if token == '(':
                num = evaluate(tokens)
            if not token.isdigit() or not tokens:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] *= num
                elif sign == '/':
                    stack[-1] /= num
                sign = token
                num = 0
            if token == ')':
                break
        return sum(stack)
    
    tokens = list(s.replace(' ', '')) + ['']
    return evaluate(tokens)

print("Результат:", calculate(expression))
