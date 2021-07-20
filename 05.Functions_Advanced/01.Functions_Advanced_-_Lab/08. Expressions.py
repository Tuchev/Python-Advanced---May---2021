def expressions(nums, current_result=0, current_expression=""):
    if not nums:
        print(f"{current_expression}={current_result}")
        return
    expressions(nums[1:], current_result+nums[0], f'{current_expression}+{nums[0]}')
    expressions(nums[1:], current_result-nums[0], f'{current_expression}-{nums[0]}')


nums = [int(el) for el in input().split(", ")]
expressions(nums)