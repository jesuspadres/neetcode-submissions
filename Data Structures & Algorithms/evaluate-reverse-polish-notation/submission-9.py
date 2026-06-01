class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                val2 = stack.pop()
                val1 = stack.pop()

                if token == "+":
                    val3 = val1 + val2
                    stack.append(val3)
                    print(val3)
                elif token == "-":
                    val3 = val1 - val2
                    stack.append(val3)
                    print(val3)
                elif token == "*":
                    val3 = val1 * val2
                    stack.append(val3)
                    print(val3)
                elif token == "/":
                    val3 = float(val1) / val2
                    stack.append(int(val3))
                    print(val3)
            else:
                stack.append(int(token))

                
        
        return stack.pop()
