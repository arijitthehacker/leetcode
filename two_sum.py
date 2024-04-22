'''
>>> twoSum([2,7,11,15], 9)
[0, 1]
>>> twoSum([3,2,4], 6)
[1, 2]
>>> twoSum([3,3], 6)
[0, 1]
'''

from typing import List


def twoSum(nums: List[int],target: int) -> List[int]:
    seen = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement not in seen:
            seen[nums[i]]=i
            continue
        return [seen[complement],i]
    return []

if __name__ == '__main__':
    import doctest
    if doctest.testmod():
        print('Passed all tests')