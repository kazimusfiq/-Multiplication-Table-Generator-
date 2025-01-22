def generate_multiplication_table(number, limit=10):
    print(f"Multiplication Table for {number}:")
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")

# Example usage
num = int(input("Enter a number: "))
generate_multiplication_table(num)
