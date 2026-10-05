def subset_sum(nums, target):
    nums = sorted(nums)
    found = []
    chosen = []

    def go(i, remaining):
        if remaining == 0:
            found.append(chosen[:])
            return

        if i == len(nums) or nums[i] > remaining:
            return  # prune

        chosen.append(nums[i])  # choose
        go(i + 1, remaining - nums[i])
        chosen.pop()  # backtrack

        go(i + 1, remaining)  # skip

    go(0, target)
    return found


print(subset_sum([3, 34, 4, 12, 5, 2], 9))
print(subset_sum([1, 2, 3], 7))