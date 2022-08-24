# https://leetcode.com/problems/rearrange-spaces-between-words/
"""
Inplace Problem:
Given string like 'abc\s\s\s def \s \s \s \s gdf \s dd '. 
Each word is separtated by different number of spaces. 
Reorder the spaces, so that there are equal number of spaces between words. 
Must be inplace. 
Put extra space to the end if there are any 
(e.g. 7 spaces 3 words should returnXXX\s\s XXX\s\s XXX\s\s\s)
"""

class Solution(object):
    def reorderSpaces(self, text):
        """
        :type text: str
        :rtype: str
        """
        # Inplace
        total_s = sum([1 if i == " " else 0 for i in text])
        if total_s == 0:
            return text
        breaks = len(text.split()) - 1
        if breaks == 0:
            mid_s = 0
        else:
            mid_s = int(total_s / breaks)
        ending_s = total_s - mid_s * breaks
        list_s = [0] + [mid_s] * breaks + [ending_s]
        text = [char for char in text] + [" "] * total_s
        print(list_s)
        
        i = 0
        j = 0
        count_s = 0
        beginning = True
        while i < len(text):
            if text[i] == " ":
                count_s += 1
                beginning = False
            else:   
                if count_s == 0:
                    i += 1
                    if beginning == True:
                        j += 1
                        beginning = False
                    continue
                if count_s > list_s[j]:
                    diff = count_s - list_s[j]
                    # move the list from i to the left diff steps
                    for t in range(i-diff, len(text)-diff):
                        text[t] = text[t+diff]
                    # fill the end diff chars as spaces
                    for t in range(len(text)-diff, len(text)):
                        text[t] = " "
                    # update i since moving left
                    i = i - diff
                elif count_s < list_s[j]:
                    diff = list_s[j] - count_s
                    # move the list from i to the right diff steps
                    for t in range(len(text)-1, i-1, -1):
                        text[t] = text[t-diff]
                    # move the list from i to i+diff with spaces
                    for t in range(i, i+diff):
                        text[t] = " "
                    # update i since moving right
                    i = i + diff
                # reset space count since hitting chars
                count_s = 0
                # update required spaces
                j += 1
            i += 1
        
        return "".join(text)[:-total_s]

        # Not inplace
        """
        tot_s = sum([1 if i == " " else 0 for i in text])
        if tot_s == 0:
            return text
        words = text.split()
        if len(words) == 1:
            num_s = 0
        else:
            num_s = int(tot_s / (len(words) - 1))
        end_s =  tot_s - num_s * (len(words) - 1)
        s = " " * num_s
        return s.join(words) + " " * end_s
        """
        