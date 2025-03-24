class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        
        undefeated = []
        almost_undefeated = []
        ans = [undefeated,almost_undefeated]
        stats = defaultdict(lambda: [0,0])
        
        for match in matches:
            winner = match[0]
            loser = match[1]
            
            stats[winner][0] += 1
            stats[loser][1] += 1
            
        for player in stats:
            if stats[player][1] == 1:
                almost_undefeated.append(player)
            
            if stats[player][0] > 0 and stats[player][1] == 0:
                undefeated.append(player)
                
            
        
        undefeated.sort()
        almost_undefeated.sort()
        return ans