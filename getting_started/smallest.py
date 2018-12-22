# values = [9, 41, 12, 3, 74, 15]
# smallest_so_far = values[0]
# print("Before", smallest_so_far)
# for value in values :
#     if value < smallest_so_far :
#         smallest_so_far = value
#     print(smallest_so_far, value)
# print("After", smallest_so_far)


smallest = None
print("Before", smallest)
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print("After", smallest)
