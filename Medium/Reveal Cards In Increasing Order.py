from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        q = deque(list(range(len(deck))))
        deck.sort()
        ans = [0] * len(deck)

        for card in deck:
            ans[q.popleft()] = card
            if q:
                q.append(q.popleft())

        return ans

