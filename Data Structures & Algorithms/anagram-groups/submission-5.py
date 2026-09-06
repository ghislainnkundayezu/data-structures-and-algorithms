from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = defaultdict(list)

        for word in strs:
            wordMap["".join(sorted(word))].append(word)
        
        return list(wordMap.values())