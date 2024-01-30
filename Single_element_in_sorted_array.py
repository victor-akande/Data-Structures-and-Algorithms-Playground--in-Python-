nums = [1,1,2,2,3,3,4,4,5,8,8]

def Solution(nums):
    """
    Finds the single element in a sorted array where all other elements appear twice.

    Args:
        nums (List[int]): The sorted array of integers.

    Returns:
        int: The single element in the array.

    """
    res = 0
    for num in nums:
        res ^= num
    return res

print(Solution(nums))