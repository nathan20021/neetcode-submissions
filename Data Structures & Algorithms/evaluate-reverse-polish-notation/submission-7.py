class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def eval_ops(s1, s2, ops):
            # return int(eval(f"{s1} {ops} {s2}"))
            s1, s2 = int(s1), int(s2)
            if ops == "+":
                return s1 + s2
            if ops == "-":
                return s1 - s2
            if ops == "*":
                return s1 * s2
            if ops == "/":
                return int(s1 / s2)

        if len(tokens) == 1:
            return int(tokens[0])

        stack = []
        OPS_VOCAB = {'+', '-', '*', '/'}
        for t in tokens:
            if t not in OPS_VOCAB:
                stack.append(t)
            else:
                s2, s1 = stack.pop(), stack.pop()
                stack.append(eval_ops(s1, s2, t))
        return stack[0]