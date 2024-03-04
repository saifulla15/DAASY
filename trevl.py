def tsp(graph):
    n = len(graph)
    all_sets = (1 << n) - 1
    memo = [[None] * n for _ in range(1 << n)]

    def tsp_helper(mask, pos):
        if mask == all_sets:
            return graph[pos][0]
        if memo[mask][pos] is not None:
            return memo[mask][pos]

        ans = float('inf')
        for city in range(n):
            if (mask >> city) & 1 == 0:
                new_cost = graph[pos][city] + \
                    tsp_helper(mask | (1 << city), city)
                ans = min(ans, new_cost)

        memo[mask][pos] = ans
        return ans

    return tsp_helper(1, 0)


graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print("Minimum cost for TSP:", tsp(graph))
