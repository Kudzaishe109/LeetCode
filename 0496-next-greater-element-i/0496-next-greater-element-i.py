class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        for num1 in nums1:
            i = nums2.index(num1) 
            seen = False
            for num2 in nums2[i+1:]:
                if num2 > num1:
                    arr.append(num2)
                    seen = True
                    break
            if not seen:
                arr.append(-1)
        return arr

        