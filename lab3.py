# 1. Power Function (Recursive)
def power(base, exp):
    if exp == 0:        # Base Case
        return 1
    else:               # Recursive Case
        return base * power(base, exp - 1)

# 2. Sum of Digits Function (Recursive)
def sum_digits(n):
    if n == 0:          # Base Case
        return 0
    else:               # Recursive Case
        return (n % 10) + sum_digits(n // 10)

# 3. Reverse String Function (Recursive)
def reverse_string(s):
    if len(s) == 0:     # Base Case
        return s
    else:               # Recursive Case
        return reverse_string(s[1:]) + s[0]

# --- Testing the Functions ---
print(f"2 to the power of 3 is: {power(2, 3)}")
print(f"Sum of digits in 123 is: {sum_digits(123)}")
print(f"Reverse of 'Hello': {reverse_string('Hello')}")