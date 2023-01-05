def twoSums(nums, target):

    cache_dict = {}
    temp_list = []

    for i in range(len(nums)):
        remainder = target - nums[i]

        if not remainder in cache_dict:
            cache_dict[nums[i]] = i  # take index
        else:
            temp_list.append(cache_dict[remainder])
            temp_list.append(i)
            return temp_list


nums = [3, 2, 4]
target = 6

print(twoSums(nums, target))
