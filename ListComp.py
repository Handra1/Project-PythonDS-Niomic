nums = [12,8,21,3,16]
new_nums = []
for num in nums :
    new_nums.append(num + 1)
print(new_nums)

"""cara yg mudah"""
new_nums = [num + 1 for num in nums]
print(new_nums)

"""list comprehensions dengan jangkauan atau range"""
result = [num for num in range(11)]
print(result)
