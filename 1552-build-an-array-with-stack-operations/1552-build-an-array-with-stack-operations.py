class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = [0] * n
        stream = [0] * n
        ans = []
        

        for i in range(n):
            stream[i] = i + 1


        # while position in stack is not equal target
        # push and pop new numbers
        stream_index = 0
        for i, num in enumerate(target):
            
            while target[i] != stack[i]:
                stack[i] = stream[stream_index]
                stream_index += 1
                ans.append("Push")
                if target[i] != stack[i]:
                    ans.append("Pop")
        return ans


