def sum_of_elements(numbers, exclude_negative=False):
    if exclude_negative:
        filtered_numbers = [num for num in numbers if num >= 0]
    else:
        filtered_numbers = numbers

    return sum(filtered_numbers)
user_input = input("Enter a list of numbers separated by spaces (e.g., 1 2 3 -4 5 -6): ")
numbers = [int(num) for num in user_input.split()]

user_choice = input("Do you want to exclude negative numbers? (yes or no): ").lower()

if user_choice == "yes":
    result = sum_of_elements(numbers, exclude_negative=True)
else:
    result = sum_of_elements(numbers)

print("Sum of elements:", result)
