def classify_numbers(numbers):
    evenNumbers = []
    oddNumbers = []

    for num in numbers:
        if num % 2 == 0:
            evenNumbers.append(num)
        else:
            oddNumbers.append(num)

    return evenNumbers, oddNumbers

inputNumbers = input("Enter a list of numbers separated by spaces: ")
numbers = [int(n) for n in inputNumbers.split()]

even, odd = classify_numbers(numbers)

print("Even numbers:", even)
print("Odd numbers:", odd)
