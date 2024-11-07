class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        if len(s)==1:
            return 1
        foundMaxLen = []
        for i in range(len(s)):
            count = 0
            seen = set()
            for j in range(i, len(s)):
                if s[j] in seen:
                    foundMaxLen.append(count)
                    break
                if j==len(s)-1 and s[j] not in seen:
                    count += 1
                    foundMaxLen.append(count)
                    break
                seen.add(s[j])
                count += 1
        return max(foundMaxLen)