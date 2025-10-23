class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start + (i * 2) for i in range(0, n)]
        xor = nums[0]
        for num in nums[1:]:
            xor ^= num
        return xor
        