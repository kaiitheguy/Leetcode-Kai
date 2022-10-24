# https://leetcode.com/problems/find-and-replace-in-string/

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        map = {}
        for i in range(len(indices)):
            index = indices[i]
            map[index] = [sources[i], targets[i]]
        res = []
        i = 0
        while i < len(s):
            if i in map.keys():
                start = i
                end = i + len(map[i][0])
                if s[start:end] == map[i][0]:
                    res.append(map[i][1])
                    i = end
                else:
                    res.append(s[i])
                    i += 1
            else:
                res.append(s[i])
                i += 1
        return "".join(res)