def a_number():
    return 5


def sum_of_two(first_number, second_number):
    return first_number + second_number

"""
this function accepts  the function a_number() 
as an argument
"""
answer = sum_of_two(a_number(), 32)

print(answer)