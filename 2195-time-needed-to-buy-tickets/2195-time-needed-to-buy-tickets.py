class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # first brute force is the simulate the queue

        time_taken = 0
        curr_position = k
        while tickets:

            front = tickets[0]
            if front > 1:
                if curr_position == 0:
                    tickets[0] -= 1
                    tickets.append(tickets.pop(0))
                    curr_position = len(tickets) - 1
                    time_taken += 1
                    continue
                tickets[0] -= 1
                tickets.append(tickets.pop(0))
                time_taken += 1
                curr_position -= 1

            elif front == 1:
                if curr_position == 0:
                    time_taken += 1
                    break
                time_taken += 1
                tickets.pop(0)
                curr_position -= 1

        return time_taken