class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_char_count = {} # O(1)
        t_char_count = {} # O(1)

        for char in s: # O(n)
            if char not in s_char_count:
                s_char_count[char] = 0
            s_char_count[char] += 1

        for char in t: # O(n)
            if char not in t_char_count:
                t_char_count[char] = 0
            t_char_count[char] += 1
        
        for char in s_char_count: # O(1)
            if char not in t_char_count:
                return False
            if s_char_count[char] != t_char_count[char]:
                return False
        
        return True
