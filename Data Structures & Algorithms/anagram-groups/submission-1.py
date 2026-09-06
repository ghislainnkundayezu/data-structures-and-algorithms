class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_hash = {}    
        for w in set(strs):
            anagram_hash[tuple(sorted(w))] = []
        print(anagram_hash)

        for a in strs:
            an = tuple(sorted(a))
            if an in anagram_hash:
                anagram_hash[an].append(a)
        
        print(anagram_hash)
        print(list(anagram_hash.values()))
        return list(anagram_hash.values())