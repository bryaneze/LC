def searchMatrix(matrix, target):
    i = 0
    while i < len(matrix):
        if target == matrix[i][-1]: # If row only has 1 element, check if it is target 
            return True
        if target > matrix[i][-1]: # If target is bigger than last element of a row, move onto next row 
            i+=1
            continue
        else: # Normal binary search
            l = 0
            r = len(matrix[i]) - 1
    
            while l <= r:
                mid = (l+r)//2
                if matrix[i][mid] > target:
                    r = mid - 1
                elif matrix[i][mid] <target:
                    l = mid + 1
                else:
                    return True
        return False
    return False



# Driver code
matrix =[[1],[2],[3]]
target = 3
print(searchMatrix(matrix, target))