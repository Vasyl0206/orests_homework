def count_positives_sum_negatives(arr):
    #your code here
    if not arr:
        return []
    else:
        num1 = 0
        num2 = 0
        for i in arr:
            if i > 0:
               num1 +=1
            elif i < 0:
               num2 = num2 + i
    return [num1, num2]
    