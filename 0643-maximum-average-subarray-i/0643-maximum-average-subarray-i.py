class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
            #Edge cases

              -k > the len(nums) => return nums
              -when k = 0, return 0
              -when k == 1, return max(nums)

            #Plan/Design

             -assign two pinters, left to index 0 and right to index k - 1
             -calculate the average 
             -move the both pointers and calculate the average, assign average to the bigger of the two.  
             -repeat until right == len(nums) - 1


        """
        if k == 1:
            return max(nums)

        winSum = 0
        for i in range(k):
            winSum += nums[i]
        
        maxSum = winSum
        
        left, right = 0, k 
        while right < len(nums):
            winSum = winSum + nums[right] - nums[left]

            right += 1
            left += 1

            maxSum = max(maxSum, winSum)
        return maxSum / float(k)

      




        