# https://leetcode.com/problems/course-schedule/

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """        
        def dfs(node):
            if visited[node] == -1:
                return False
            elif visited[node] == 1:
                return True
            visited[node] = -1
            for n in graph[node]:
                if not dfs(n): return False
            visited[node] = 1
            return True
        
        graph = collections.defaultdict(set)
        for i, j in prerequisites:
            graph[i].add(j)
        
        visited = [0 for _ in range(numCourses)]
        for n in range(numCourses):
            if not dfs(n): return False
        
        return True