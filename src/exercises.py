def reverse_list(input_list):
    """
    Reverses order of elements in list input_list.
    """
    n = len(input_list)
    output_list= [0]*n
    i=0
    j=n-1
    for ele in input_list:
        output_list[j]=ele
        j -= 1

    return output_list

def count_digits(number):
    """
    Return count of digits
    """
    if number == 0:
        return 1

    count = 0
    while number > 0:
        number /= 10
        count += 1

    return count



# print(reverse_list([1,2,3]))
# print(count_digits(1))
