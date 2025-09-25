class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        x = abs(x)

        r_str_x = str(x)[::-1]
        unsigned_x = int(r_str_x)
        result = sign * unsigned_x
        if result < -2 **31 or result > 2 **31 -1:
            return 0
        return result 



        