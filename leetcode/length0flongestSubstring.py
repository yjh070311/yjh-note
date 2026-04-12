def lengthOfLongestSubstring(self,s):
    left=0
    max_len=0
    s_index={}
    for right,char in enumerate(s):
        if char in s_index and s_index[char]>=left:
            left=s_index[char]+1
        s_index[char]=right
        max_len=max(max_len,right-left+1)
        
    return max_len