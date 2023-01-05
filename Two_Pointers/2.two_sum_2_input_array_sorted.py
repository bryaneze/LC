def twoSum(numbers, target):
    leftP = 0
    rightP = len(numbers) - 1

    while numbers[rightP] > target and target >= 0 and numbers[leftP] > 0:
        rightP -= 1
    while leftP <= rightP:
        if numbers[leftP] + numbers[rightP] == target:
            return [leftP + 1, rightP + 1]

        if numbers[leftP] + numbers[rightP] < target:
            leftP += 1
        else:
            rightP -= 1


nums = [5, 25, 75]
print(twoSum(nums, 100))
