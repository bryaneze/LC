def topKFrequent(nums, k):

    temp_dict = {}
    for i in nums:
        if i not in temp_dict:
            temp_dict[i] = 1
        else:
            temp_dict[i] += 1
    bucket = [[] for i in range(len(nums) + 1)]

    for v, c in temp_dict.items():
        bucket[c].append(v)

    res = []
    for i in range(len(bucket) - 1, 0, -1):
        res.extend(bucket[i])
        if len(res) == k:
            return res


nums = [5, 1, 3, 6, 5, 8, 8, 2, 5]

print(topKFrequent(nums, 2))
