def equalStacks(h1, h2, h3):
    stacks = (list(reversed(h1)), list(reversed(h2)), list(reversed(h3)))
    heights = [sum(stack) for stack in stacks]
    min_height = min(heights)
    while min_height != max(heights):
        for i in range(3):
            while heights[i] > min_height:
                heights[i] -= stacks[i].pop()
        min_height = min(heights)
    return min_height