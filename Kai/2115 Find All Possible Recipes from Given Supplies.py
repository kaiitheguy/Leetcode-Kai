# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

from collections import defaultdict

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = defaultdict(list)
        for i, recipe in enumerate(recipes):
            indegree[recipe] = 0
            for ingredient in ingredients[i]:
                if ingredient not in supplies:
                    graph[ingredient].append(recipe)
                    indegree[recipe] += 1
        queue = []
        visited = set()
        for recipe in indegree.keys():
            if indegree[recipe] == 0:
                queue.append(recipe)
                visited.add(recipe)
        while queue:
            recipe = queue.pop(0)
            for sub_recipe in graph[recipe]:
                indegree[sub_recipe] -= 1
                if indegree[sub_recipe] == 0 and sub_recipe not in visited:
                    queue.append(sub_recipe)
                    visited.add(sub_recipe)
        return list(visited)            
        