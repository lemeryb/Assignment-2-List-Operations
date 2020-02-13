# Title: Assignment 2 List Operations
# Author: Benjamin Lemery
# Date: 2/11/20
# Description:

user_inputs = []

# Generates our number list with the user input
print("\nYou will enter five numbers. Please enter the numbers one at a time.\n")
for num_of_list_indices in range(0,5):
    list_index = int(input("Enter a number: "))
    user_inputs.append(list_index)


# Sorts the values the user inputted in a list from least to greatest.
def sort_numbers(user_inputs):
    print("\nThe five values you just entered will be sorted into a list from least to greatest.")
    user_inputs.sort()
    print(user_inputs)
    get_sum_of_numbers(user_inputs)


# Gets the total sum of all of the numbers in the list
def get_sum_of_numbers(user_inputs):
    sum = 0
    for user_input in range(len(user_inputs)):
        sum += user_inputs[user_input]
    print("\nThe sum of all of the values in the list is: " + str(sum))
    get_product_of_numbers(user_inputs)


# Gets the total multiplied value of all of the numbers in the list.
def get_product_of_numbers(user_inputs):
    product = 1
    for user_input in range(len(user_inputs)):
        product *= user_inputs[user_input]
    print("\nThe product of all of the values in the list is: " + str(product))
    get_mean_of_numbers(user_inputs)


# Gets the mean value of the list
def get_mean_of_numbers(user_inputs):
    sum = 0
    for user_input in range(len(user_inputs)):
        sum += user_inputs[user_input]
    mean = sum / len(user_inputs)
    print("\nThe mean of all of the values in the list is: "+ str(mean))
    get_median_of_numbers(user_inputs)


# Gets the median value of the list
def get_median_of_numbers(user_inputs):
    get_index_of_median = user_inputs[2]
    print("\nThe median of all of the values in the list is: " + str(get_index_of_median))
    get_largest_number(user_inputs)


# Gets the largest number in the list
def get_largest_number(user_inputs):
    print("\nThe largest number in the list is: " + str(user_inputs[-1]))
    get_smallest_number(user_inputs)


# Gets the smallest number in the list
def get_smallest_number(user_inputs):
    print("\nThe smallest number in the list is: " + str(user_inputs[0]))
    remove_duplicates(user_inputs)


# Removes any duplicate values within the list
def remove_duplicates(user_inputs):
    new_list = []
    for i in user_inputs:
        if i not in new_list:
            new_list.append(i)
    print("\nThis is the list without any duplicate values: " + str(new_list))
    remove_even_numbers(user_inputs)

# The following two functions use a technique called "List Comprehension" to effectively generate a new list that removes the even/odd numbers.


# Removes all of the even numbers from the list
def remove_even_numbers(user_inputs):
    print("\nThis is the list without any of the even numbers: " + str([user_input for user_input in user_inputs if user_input % 2 !=0]))
    remove_odd_numbers(user_inputs)


# Removes all of the odd numbers from within the list
def remove_odd_numbers(user_inputs):
    print("\nThis is the list without any of the odd numbers: " + str([user_input for user_input in user_inputs if user_input % 2 == 0]))
    enter_another_number(user_inputs)


# Asks the user to enter another number to compare to the existing list values.
def enter_another_number(user_inputs):
    new_number = int(input("\nA new number needs to be entered. This new number will be compared to the existing numbers in the list. \nEnter a new number: "))
    print("\nHere is your whole list again for reference: " + str(user_inputs))
    if new_number in user_inputs:
        print("The number " + str(new_number) + " is in the list.")
    else:
        print("The number " + str(new_number) + " is not in the list.")
    get_second_largest_number(user_inputs)


# Gets the second largest number in the list
def get_second_largest_number(user_inputs):
    print("\nThe second largest number in your list is: " + str(user_inputs[-2]))


# Calls the first function of the script to sort the list values appropriately.
sort_numbers(user_inputs)