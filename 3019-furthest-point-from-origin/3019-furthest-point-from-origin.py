class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        freq = {}

        for move in moves:
            if move not in freq:
                freq[move] = 0
            freq[move] += 1
        
        if len(freq) == 1:
            return freq[moves[0]]

        diff = abs(freq.get('L', 0) - freq.get('R', 0))

        if '_' in freq:
            return diff + freq['_']
        return diff
