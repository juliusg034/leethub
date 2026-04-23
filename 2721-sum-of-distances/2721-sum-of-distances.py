class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        position_map = {}
        res = [0] * n

        for index, num in enumerate(nums):
            if num not in position_map:
                position_map[num] = []
            position_map[num].append(index)

    
        for num, positions in position_map.items():
            k = len(positions)
            if k == 1:
                continue
            
            k = len(positions)
            prefix = [0] * k
            prefix[0] = positions[0]

            for i in range(1, k):
                prefix[i] = prefix[i-1] + positions[i]

            total_sum = prefix[-1]

            for i, pos in enumerate(positions):
                left_count = i
                right_count = k - i - 1

                left_sum = prefix[i] - pos
                right_sum = total_sum - prefix[i]

                res[pos] = (pos * left_count - left_sum) + (right_sum - pos * right_count)
        return res



            

