number_list =[-15, 23, 34, 45, 65, 100, 34]

def find_min(number_list):
    min_val= number_list[0]
    for i in range(len(number_list)):
        if number_list[i]<= min_val:
            min_val = number_list[i]
    return min_val
print(find_min(number_list))


# number_list=[65,12,15,23,34,45,65,100,27]

# number_list.sort()
# print(number_list)
# num1=number_list.pop()
# print("max value is",num1)
# print("min value is", number_list[0])