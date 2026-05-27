class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            stones.sort()
            total = stones.pop() - stones.pop()
            if total > 0:
                stones.append(total)

        if stones:
            return stones[0]
        else:
            return 0
