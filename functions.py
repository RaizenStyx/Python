# Finding max value in list
def max_val(num_list):
    maxvalue = 0
    for num in num_list:
        if num > maxvalue:
            maxvalue = num
    return maxvalue


def add_2_ints(a, b):
    return a+b


def compute_list_avg(numb_list):
    return sum(numb_list) / len(numb_list)


def celsius_to_fahrenheit(cel_degrees):
    return cel_degrees * 1.8 + 32


