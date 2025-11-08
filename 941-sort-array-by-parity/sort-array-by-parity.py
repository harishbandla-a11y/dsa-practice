class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = []

        while left <= right:
            if nums[left]% 2 ==0:
                result.append(nums[left])
                left+=1

            elif nums[right]%2 ==0:
                result.append(nums[right])
                right-=1

            else:
                right-=1
                 
        for n in nums:
            if n % 2 != 0:
                result.append(n)


        return result
           
