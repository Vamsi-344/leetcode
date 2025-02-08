class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            if -(2**31) <= -self.abs_reverse(abs(x)) <= (2**31)-1:
                return -self.abs_reverse(abs(x))
            else:
                return 0
        else:
            if -(2**31) <= self.abs_reverse(abs(x)) <= (2**31)-1:
                return self.abs_reverse(abs(x))
            else: 
                return 0

    def abs_reverse(self, x: int) -> int:
        i = 0
        res = 0
        while x > 0:
            # print(res*10)
            # print(x%10)
            res = res*10 + (x%10)
            # print(res)
            x = x//10
            i += 1
        return res
