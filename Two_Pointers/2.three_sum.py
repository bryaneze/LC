
def threeSum(nums):
    res = []
    nums.sort()
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue 

        l, r = i+1, len(nums) -1
        while l < r:
            sum = a + nums[l] + nums[r]
            if sum > 0:
                r -=1 
            elif sum < 0:
                l +=1
            else:
                res.append([a, nums[l], nums[r]])
                l+=1
                while nums[l] == nums[l-1] and l < r:
                    l+=1
    return res 





# Own solution; not working
def threeSum_own(nums):

    def mergeSort(arr):
        if len(arr) == 1:
            return arr
        
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        left = mergeSort(left)
        right = mergeSort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i+=1
                k+=1
            else:
                arr[k] = right[j]
                j+=1
                k+=1
        
        while i < len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1
        return arr
    nums = mergeSort(nums)

    a = 0 
    l = a+1
    r = len(nums) - 1
    res = []
    
    while nums[l] == nums[a]:
        l+=1 
    while l < r:
        sum = nums[a] + nums[l] + nums[r]
        if sum > 0:
            r-=1
        elif sum < 0:
            l+=1
        else:
            res.append([nums[a], nums[l], nums[r]])
            l+=1
            while nums[l] == nums[l - 1] and l < r:
                l+=1 
   
    

    return res


nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))



