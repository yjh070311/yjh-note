class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s)<len(p):
            return []
        result=[]
        s_len=len(s)
        p_len=len(p)
        diff=[0]*26
        for char in p:
            diff[ord(char)-ord('a')]+=1
        for i in range(p_len):
            diff[ord(s[i])-ord('a')]-=1
        if all(x==0 for x in diff):
            result.append(0)

        for i in range(p_len,s_len):
            left_char =s[i-p_len]
            diff[ord(left_char)-ord('a')]+=1

            right_char=s[i]
            diff[ord(right_char)-ord('a')]-=1

            if all(x==0 for x in diff):
                result.append(i-p_len+1)

        return result