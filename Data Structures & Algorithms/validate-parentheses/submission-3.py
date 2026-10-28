class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        pairLookUp = {
            "{" : "}",
            "(" : ")",
            "[" : "]",
        }


        stack = deque()
        s_len = len(s)
        is_len_odd = (s_len % 2) == 1
        if is_len_odd:
            return False
        i = 0
        while i in range(s_len):
            if s[i] in pairLookUp:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                right_param = stack.pop()
                if s[i] != pairLookUp[right_param]:
                    return False
            i += 1
        if len(stack) > 0:
            return False
        return True
        

        