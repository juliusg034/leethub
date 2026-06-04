from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque(range(len(tickets)))
        time_taken = 0

        while queue:
            person = queue.popleft()
            tickets[person] -= 1
            time_taken += 1

            if person == k and tickets[person] == 0:
                return time_taken

            if tickets[person] > 0:
                queue.append(person)