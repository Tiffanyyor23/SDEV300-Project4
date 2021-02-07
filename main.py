import numpy as np
import re

phone_number_regex = re.compile(r'(\d\d\d-\d\d\d-\d\d\d\d)')  # that r makes it raw string
zip_code_regex = re.compile(r'(\d\d\d\d\d-\d\d\d\d)')

menu_options = {
    "a:": "Addition",
    "b:": "Subtraction",
    "c:": "Matrix Multiplication",
    "d:": "Element by element multiplication"
}


def check_if_value_is_numeric(value):
    # This function ensures the value is numeric and presented as a integer.
    while True:
        if len(value) == 3 and value.isnumeric():
            break
        value = input("The value you provided is not valid.  Please enter a numeric value")
    return value


def obtain_matrix_input(number):
    """ The purpose of this function is to collect user input and generate
    the necessary matrices
    """
    matrix_list = []
    counter = 0
    matrix_input = check_if_value_is_numeric(input("Please enter your first 3 x 3 matrix three numbers at at time: "))
    for number in matrix_input:
        matrix_list.append(int(number))
        matrix_array = np.array([matrix_list])
    while counter < 2:
        matrix_list = []
        matrix_input = check_if_value_is_numeric(input("Please enter your next 3 x 3 matrix three numbers at at time: "))
        for number in matrix_input:
            matrix_list.append(int(number))
        matrix_array = np.append(matrix_array, [matrix_list], 0)
        counter += 1
    print(f'Your {number} matrix is')
    print(matrix_array)
    return matrix_array


def add_matrices(matrix_one, matrix_two):
    """ The purpose of the function is to add 2 matrices"""
    addition_output = np.add(matrix_one, matrix_two)
    print(addition_output)
    return addition_output


def subtract_matrices(matrix_one, matrix_two):
    """ The purpose of this function is to subtract 2 matrices"""
    subtraction_output = np.subtract(matrix_one, matrix_two)
    print(subtraction_output)
    return subtraction_output


def multiply_matrices(matrix_one, matrix_two):
    """ The purpose of this function is to multiply 2 matrices"""
    multiplication_output = np.multiply(matrix_one, matrix_two)
    print(multiplication_output)
    return multiplication_output


def multiply_matrices_by_elements():
    """ The purpose of this function is to multiply specific elements of matrices"""
    pass


def transpose_matrix(matrix):
    """ The purpose of this function to to transpose the provided matrix"""
    transpose = np.transpose(matrix)
    print("The transpose is: ")
    print(transpose)


def row_mean(matrix):
    """ The purpose of this function is to calculate the mean value of each row in the provided matrix"""
    add = 0
    counter = 0
    row_mean_list = []
    while counter != 3:
        for x in matrix:
            add = add + x[counter]
        add = add // 3
        counter = counter + 1
        row_mean_list.append(add)
    print(f'Row: {row_mean_list[0]}, {row_mean_list[1]}, {row_mean_list[2]}')


def column_mean(matrix):
    """ The purpose of this function is to calculate the mean value of each column in the provided matrix"""
    column_mean_list = []
    for row in matrix:
        add = row[0] + row[1] + row[2]
        add = add // 3
        column_mean_list.append(add)
    print(f'Column: {column_mean_list[0]}, {column_mean_list[1]}, {column_mean_list[2]}')


print("Welcome to the Matrix Application.")
play_game = input("Would you like to play the Matrix Game? Enter Yes or No: ").lower()
while play_game == 'yes':
    first_matrix = obtain_matrix_input('First')
    second_matrix = obtain_matrix_input('Second')
    print("Please select an operation, from the below, to perform on your matrices.")
    for choice, option in menu_options.items():
        print(f'{choice} : {option}')
    selection = input("Selection: ")
    if selection == "a":
        print("You have selected to add matrices.  Below are the results of the operation.")
        print("The output for this operation is below \n")
        answer = add_matrices(first_matrix, second_matrix)
        transpose_matrix(answer)
        row_mean(answer)
        column_mean(answer)
    elif selection == "b":
        print("You have selected to subtract matrices.  Following are the results of the operation")
        answer_b = subtract_matrices(first_matrix, second_matrix)
        transpose_matrix(answer_b)
        row_mean(answer_b)
        column_mean(answer_b)
    elif selection == "c":
        print("You have selected to multiply matrices.  Following are the results of the operation")
        answer_c = multiply_matrices(first_matrix, second_matrix)
        transpose_matrix(answer_c)
        row_mean(answer_c)
        column_mean(answer_c)
    elif selection == "d":
        print("You have selected to do element by element multiplication  Following are the results of the operation")
        answer_d = multiply_matrices_by_elements()

    else:
        pass
    play_game = input("Do you want to play the Matrix Game, again? Enter Yes or No: ")
print("Thank you for playing. \n Good bye")
