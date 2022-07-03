def highest_product(array):

    sorted_array = sorted(array, reverse=True)
    last_index = len(sorted_array) - 1
    
    case1 = sorted_array[0] * sorted_array[1] * sorted_array[2]
    case2 = sorted_array[last_index] * sorted_array[last_index - 1] * sorted_array[0]

    return max(case1, case2)

print(highest_product([-5,-2,-1,0,0,3,4,5]))
print(highest_product([-5,-2,-1,0,0,1,1,5]))