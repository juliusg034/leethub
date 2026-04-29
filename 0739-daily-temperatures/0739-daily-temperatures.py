class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        dec_stack = []

        for i in range(len(temperatures)):
            while dec_stack and temperatures[dec_stack[-1]] < temperatures[i]:
                j = dec_stack.pop()
                res[j] = i - j
            dec_stack.append(i)
        return res