def find_missing_number(numbers):
    sum_of_numbers = sum(numbers)
    length = len(numbers)
    n = length + 1
    
    sum_of_n_integers = n * (n + 1) // 2
    
    missing_number = sum_of_n_integers - sum_of_numbers
    
    return missing_number

