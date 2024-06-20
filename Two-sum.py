def twosum(nums: list[int], target: int) -> bool:
    hasmap = {}

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hasmap:
            return [i, hasmap[complement]]
        hasmap[nums[i]] = i
    return hasmap

nums = [2,7,11,15]
target = 9

print(twosum(nums, target))