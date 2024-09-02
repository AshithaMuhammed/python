arr=[
    [10,11,12],
    [12,13,14],
    [15,16]
]
# print all numbers>11
numbers_filter=num_gt_11=[num for lst in arr for num in lst if num>11]
print(num_gt_11)
