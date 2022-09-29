# https://leetcode.com/problems/course-schedule-ii/

#from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        indegree = {}
        for i in range(numCourses):
            graph[i] = []
            indegree[i] = 0
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1
        queue = []
        order = []
        for node in indegree.keys():
            if indegree[node] == 0:
                queue.append(node)
        while queue:
            node = queue.pop()
            order.append(node)
            for neighbour in graph[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        if len(order) != numCourses:
            return []
        else:
            return order
        