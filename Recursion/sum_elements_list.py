
#Finding the sum of elements in a list
my_list=[1, 3, 5, 7, 9]

def list_sum(list_num):
    the_sum=0
    
    for i in list_num:
        the_sum+=i
    return the_sum

# print(list_sum(list_num=my_list))

#Assume we had no loops and we want to find the sum of elements in a list
# We would have something like (1+(3+(5+(7+9)))

def list_sum2(num_list):
    #preconditions
    if len(num_list)==1:
        return num_list[0]
    else:
        print('hi')
        return num_list[0]+list_sum2(num_list[1:])  #recursion
    
# print(f"Sum 2: {list_sum2(my_list)}")


conv_string="0123456789"
print(type(conv_string[9]))