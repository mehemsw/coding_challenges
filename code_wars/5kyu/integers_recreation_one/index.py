import math

def list_squared(m, n):
#     Find divisors of a number
    list_of_answers = []
    for idx1 in range(m, n):
        squared_divisors_list = [ idx ** 2 for idx in range(1, idx1 + 1) if idx1 % idx == 0 ]
        squared_sum = sum(squared_divisors_list)
        square_root = math.sqrt(squared_sum)
        int_check = square_root.is_integer()
        if int_check:
            list_of_answers.append([idx1, squared_sum])
    return list_of_answers
print(list_squared(42, 250))

# This code needs to be optimized. It takes too long to execute.
