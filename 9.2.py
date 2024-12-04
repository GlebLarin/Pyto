def find_max_recursive():
    try:
        num = int(input())
        if num == 0:
            return 0 
        else:
            max_so_far = find_max_recursive() # Recursive call
            return max(num, max_so_far) if max_so_far != 0 else num 
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return find_max_recursive() 
    max_value = find_max_recursive()
    if max_value!= 0:
     print("The maximum value is:", max_value)
