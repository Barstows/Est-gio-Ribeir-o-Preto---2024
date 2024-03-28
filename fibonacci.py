def contains_number_fibonacci(n):
    sequence = [0,1]
    while sequence[-1]<n:
        sequence.append(sequence[-1] +sequence[-2])
    return sequence

def check_if_cointaned(num, sequence):
    if num in sequence:
        return True
    else:
        return False

input_num= int(input("Input number: "))
sequence = contains_number_fibonacci(input_num)

if check_if_cointaned(input_num, sequence):
    print(f"The number {input_num} doesnt belong in Fibonacci.")
else:
    print(f"The number {input_num} belongs in Fibonacci.")
