# https://leetcode.com/problems/maximal-network-rank/

from collections import defaultdict

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        road_dict = defaultdict(set)
        for a, b in roads:
            road_dict[a].add(b)
            road_dict[b].add(a)
        max_rank = 0
        for i in range(n):
            for j in range(i+1, n):
                rank = len(road_dict[i]) + len(road_dict[j])
                if i in road_dict[j]:
                    rank -= 1
                max_rank = max(max_rank, rank)
        return max_rank
        