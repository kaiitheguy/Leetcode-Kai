# https://leetcode.com/problems/sentence-screen-fitting/

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        i = 0
        j = 0
        k = 0
        count = 0
        memo = {}
        while i < rows:
            if sentence[k] in memo.keys():
                temp_count, k = memo[sentence[k]]
                count += temp_count
            else:
                temp_count = 0
                ori_k = k
                while j < cols:
                    if cols - j < len(sentence[k]):
                        break
                    j += len(sentence[k]) + 1
                    k += 1 
                    if k == len(sentence): 
                        k = 0
                    temp_count += 1
                count += temp_count
                memo[sentence[ori_k]] = [temp_count, k]
            i += 1
            j = 0
        return count // len(sentence)
                
                
                