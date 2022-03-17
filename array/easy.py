#remove duplicate
def duplicateNum(nums):
    left = 1
    right = len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        count = 0
        count = sum(num<= mid for num in nums)

        if count > mid:
            duplicate = mid
            right = mid - 1
        else:
            left = mid + 1
    return duplicate 





#rotate image
def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i] = matrix[i][::-1]