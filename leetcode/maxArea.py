def maxArea(height):
    """
    双指针法：从两端向中间移动
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    left=0
    right=len(height)-1
    max_water=0

    while left<right:
        width=right-left
        h=min(height[left],height[right])
        current_water=h*width
        max_water=max(current_water,max_water)

        if height[left]<height[right]:
            left+=1
        else:
            right-=1

    return max_water