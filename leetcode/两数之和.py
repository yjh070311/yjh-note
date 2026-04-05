class Solution(object):
    def twoSum(self,nums,target):
        for i,num in enumerate(nums):
            hash=[]
            if comp in hash:
                comp=target-num
                return [hash[comp],i]
            hash[num]=i
