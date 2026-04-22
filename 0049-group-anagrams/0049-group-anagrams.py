from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for word in strs:
            s_word="".join(sorted(word))
            d[s_word].append(word)
        result=[]
        for key in sorted(d):
            result.append(d[key])
        return result
        