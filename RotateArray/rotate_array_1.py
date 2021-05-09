class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        length = len(nums)
        new=[0]*length

        for i in range(length):
            new[(i+k)%length] = nums[i]
        
        return new
      
#       O(n) time and space

