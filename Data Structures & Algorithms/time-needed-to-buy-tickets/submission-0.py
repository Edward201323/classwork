class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        k_ptr = k
        seconds = 0
        while tickets:
            front = tickets.pop(0) - 1
            seconds += 1
            if front > 0:
                tickets.append(front)

            if k_ptr == 0 and front == 0:
                return seconds

            k_ptr = (k_ptr - 1) % len(tickets)

        return seconds