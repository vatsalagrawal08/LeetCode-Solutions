class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        result = []
        count_p = {}
        for char in p:
            count_p[char] = count_p.get(char, 0) +1
        left = 0
        count_s = {}
        for right in range(len(s)):
            count_s[s[right]] = count_s.get(s[right], 0)+ 1
            if right - left +1 >len(p):
                count_s[s[left]] -= 1
                if count_s[s[left]] == 0:
                    del count_s[s[left]]
                left += 1
            if count_s == count_p:
                result.append(left)
        return result
        
        