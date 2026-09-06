from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for i in strs:
            s = "".join(sorted(i))
            if s in group:
                group[s].append(i)
            else:
                group[s] = [i]

        return list(group.values())