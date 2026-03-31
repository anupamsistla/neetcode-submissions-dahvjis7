class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = float("-infinity")
        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()

                area = (i-index)*height
                maxArea = max(maxArea, area)
                start = index
            stack.append((start,h))

        while stack:
            i, h = stack.pop()

            area = (len(heights)-i)*h
            maxArea = max(maxArea, area)
        return maxArea