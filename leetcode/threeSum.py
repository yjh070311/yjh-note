class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        n=len(nums)
        nums.sort()
        for i in range(n-2):
            if nums[i]==nums[i-1] and i>0:
                continue
            if nums[i]+nums[i+1]+nums[i+2]>0:
                break
            left=i+1
            right=n-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if sum>0:
                    right-=1
                elif sum<0:
                    left-=1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left+1]==nums[left]:
                        left+=1                    
                    while left<right and nums[right-1]==nums[right]:
                        right-=1

                    left+=1
                    right-=1
        return result    