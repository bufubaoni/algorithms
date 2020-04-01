from collections import Counter
class Solution(object):
    def topKFrequent(self, words, k_n):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        words_count = Counter(words)

        lst_words = [(k, v) for k, v in words_count.items()]

        lst_words.sort(key=lambda x: (-x[1], x[0]))

        lst_words = [item[0] for item in lst_words]
        
        return lst_words[:k_n]

# 统计出现的频率，然后排两次序