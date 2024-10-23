class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        for i in s.split(' '):
            if i=="":
                continue
            words.append(i)
        return ' '.join(words[::-1])