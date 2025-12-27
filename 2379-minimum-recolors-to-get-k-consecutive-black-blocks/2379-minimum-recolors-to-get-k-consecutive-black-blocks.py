class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        use a window of size k and in each window find the number of W then re-
        turn the min number of  W in a certain window.

        example:

        input:: k = 4, block = "WBBWWWBBB"
        output => 1

        #design:
            -find the number of 'W' in the first k-size window 
            -store the min number of w for all the windows
            

        """
        wWinCount = 0
        for i in range(k):
            if blocks[i] == "W":
                wWinCount += 1
        minOpns = wWinCount
        left = 0
        for right in range(k,len(blocks)):
            if blocks[right] == "W":
                wWinCount += 1
            if blocks[left] == "W":
                wWinCount -= 1
            minOpns = min(minOpns, wWinCount)
            left += 1
        return minOpns


        
        
