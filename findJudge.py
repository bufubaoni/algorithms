class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if not trust:
            return 1
        graph = {}
        al = set(range(1, N+1))
        for x, y in trust:
            tru = graph.get(x, set())
            tru.add(y)
            graph[x] = tru

        x = al - set(graph.keys())
        if not x:
            return -1

        k = reduce(lambda x, y: x & y, graph.values())

        if x == k:
            return x.pop()
        return -1
