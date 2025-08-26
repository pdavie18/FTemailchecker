def add_numbers(a: int, b: int) -> int:
    total = a + b
    return total

numbers = [1, 2, 3, 4, 5,9,3]
result = add_numbers(sum(numbers[:3]), sum(numbers[3:]))

print(f"The result is {result}")
