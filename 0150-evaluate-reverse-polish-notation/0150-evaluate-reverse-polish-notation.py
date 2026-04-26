class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []


        for token in tokens:
            match token:
                case "+":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b+a)
                case "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b-a)
                case "*":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b*a)
                case "/":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b/a))
                case _:
                    stack.append(int(token))

        res = []
        while stack:
            res.append(stack.pop())
        return int("".join(map(str, res)))

        
