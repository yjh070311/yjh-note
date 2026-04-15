class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result=0
        hash=defaultdict(int)
        prefixsum=0
        hash[0]=1
        for num in nums:
            prefixsum+=num
            diff=prefixsum-k
            if diff in hash:
                result+=hash[diff]

            hash[prefixsum]+=1

        return result