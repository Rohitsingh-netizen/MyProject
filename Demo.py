
numbers = [1, 2, 3, 4, 5]
largest_number = numbers[0]  # Assume the first number is the largest initially
for num in numbers:
    if num > largest_number:
      largest_number = num
print("The largest number in the list is:", largest_number)