class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            if -(2**31) <= -int(str(abs(x))[::-1]) <= (2**31) -1:
                return -int(str(abs(x))[::-1])
            else:
                return 0
        else:
            if -(2**31) <= int(str(abs(x))[::-1]) <= (2**31) -1:
                return int(str(abs(x))[::-1])
            else:
                return 0