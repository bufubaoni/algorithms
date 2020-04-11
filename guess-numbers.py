class Solution(object):
    def game(self, guess, answer):
        """
        :type guess: List[int]
        :type answer: List[int]
        :rtype: int
        """
        count = 0
        for idx, item in enumerate(guess):
            if item == answer[idx]:
                count += 1
        return count

# 这可能是遇到的最简单的一道题了