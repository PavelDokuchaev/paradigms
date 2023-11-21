def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)

numbers = [4, 2, 9, 1, 5]
sort_numbers = sort_list_declarative(numbers)
print(sort_numbers)