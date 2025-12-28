def is_armstrong_number(number):
    is_armstrong = False

    i = number
    num_digits = 0
    while i!=0:
        i=i//10
        num_digits+=1

    print(num_digits)
    
    
    # base case
    if (number < 10) & (number > -10):
        is_armstrong = True
    else:
        temp_num = number
        sum = 0
        while temp_num != 0:
            if (temp_num < 10) & (temp_num > -10):
                ones = temp_num
            else:
                ones = temp_num % 10
            print(ones)
            sum = sum + ones**num_digits
            temp_num = temp_num//10
            print(sum)
        if sum == number:
            is_armstrong = True

    return is_armstrong