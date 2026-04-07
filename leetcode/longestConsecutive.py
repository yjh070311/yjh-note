class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set=set(nums)
        longest=0
        for num in num_set:
            if num-1 not in num_set:
                current_len=1
                current_num=num
                while current_num in num_set:
                    current_len+=1
                    current_num+=1
                
                longest=max(longest,current_len)

        return longest