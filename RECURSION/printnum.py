# Print numbers 1 to N

# Without loop

def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)
