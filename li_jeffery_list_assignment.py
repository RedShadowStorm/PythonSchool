"""
-------------------------------------------------------------------------------
Name:		list_assignment.py
Purpose:
A bunch of functions testing my knowledge of lists.

Author:		Li.J

Created:    01/05/2017
------------------------------------------------------------------------------
"""

def two23(num_list):
    """
    Checks if there are at least 2 occurences of either 2 or 3 in num_list.
    :param num_list: list - list of integers
    :return: boolean - whether or not there are two occurences of 2 or 3 occurences of 3
    """
    # Define the number of occurences of 2 and the number of occurences of 3 in the list
    num_of_2 = 0
    num_of_3 = 0

    # Iterate through the elements of num_list
    for num in num_list:

        # Increment num_of_2 if the current element is 2
        if num == 2:
            num_of_2 += 1

        # Increment num_of_3 if the current element is 3
        elif num == 3:
            num_of_3 += 1

    # Return whether or not there are two occurences of 2 or 3 occurences of 3
    return  num_of_2 >= 2 or num_of_3 >= 3

def tenStreak(num_list):
    """
    Makes multiples of 10 replace all of the list elements after them, until another mutiple of 10 is encountered
    :param num_list: list - list of integers
    :return num_list: list - the inputted list of integers, now with the tenstreak format
    """

    # Define multiple the current multiple of 10 to be an integer
    multiple = 10

    # Set seen_multiple to be False, because this is so that the tenstreak will occur only when a multiple of 10 has
    # actually been encountered
    seen_multiple = False

    # Iterate through num_list
    for i in range(len(num_list)):

        # Check if the current value of num_list is evenly divisible by zero, if so, seen_multiple is set to be True,
        # and the current multiple is set to be the current value
        if num_list[i]%10 == 0:
            multiple = num_list[i]
            seen_multiple = True

        # If a multiple has been seen, the
        elif seen_multiple:
            num_list[i] = multiple

    # Return the tenstreak formatted num_list
    return num_list

def acromatch(acronym_1, acronym_2):
    """
    :param acronym_1: list - A list of words that will form an acronym
    :param acronym_2: list - Another list of words that will form an acronym
    :return: boolean - whether the 2 acronyms match each other or not
    """

    # Checks if both acronyms are equal in number of words
    if len(acronym_1) == len(acronym_2):

        # Iterate through the length of acronym_1
        for i in range(len(acronym_1)):

            # Compare the first letter in a word of acronym_1 to that of acronym_2
            if acronym_1[i][1] != acronym_2[i][1]:

                # If they aren't equal, return False
                return False

    # Return True since all of the first letters are equal
    return True

def canVote(birth):
    """
    Checks if someone is able to vote if the minumum age is 18, and the vote occurs on 11 Nov 2017
    :param birth: String - Person's birthday in the order of "month/day/year"
    :return: Boolean - Whether the person can vote or not
    """

    # Define the youngest month, day, and year a person could vote on
    youngest_month = 11
    youngest_day = 8
    youngest_year = 1998

    # Split the birth string into a list
    birth_list = birth.split("/")

    # Turn all of the elements in birth_list to integers
    for i in range(3):
        birth_list[i] = int(birth_list[i])

    # Unpack birth_list into 3 birth variables, each carrying a different unit of time
    birth_month, birth_day, birth_year = birth_list

    # Check if the birth year is older than the youngest year
    if birth_year < youngest_year:
        return True

    # Check if the birth month is older than the youngest month, as long as the birth year is equal to the youngest year
    elif birth_month < youngest_month and birth_year == youngest_year :
        return True

    # Check if the birth day is older or the same as the youngest year as long as the birth month is the same as the youngest month
    elif birth_day <= youngest_day and birth_month == youngest_month:
        return True

    # If none of the above conditions are met, the person is to young to vote
    else:
        return False


def print_pascal(width, height):
    """
    Prints out a chart that has a rectangular section of the pascal triangle, with the top tip of the triangle at the
    top left corner of the rectangle.
    :param width:
    :param height:
    """

    # Create table filled with the number 1
    try:
        pascal_list = [[1 for column in range(width)] for row in range(height)]

    # Print out an error message if either width or height aren't integers
    except ValueError:
        print("Width and height must be integers!")


    # Iterate through the rows vertically
    for row in range(1,height):

        # Iterates through the columns in the row
        for column in range(1, width)

            # Define the values above and to the left of the current number
            above = (pascal_list[row -1][column])
            left = (pascal_list[row][column - 1])

            # Fill list elements after the first row and the first column with the sum of the number above and to the left of it
            pascal_list[row][column] = above + left

    # Iterate through the rows vertically
    for row in range(height):

        # Iterates through the columns in the row
        for column in range(width):

            # Convert all of the elements in pascal_list to strings
            pascal_list[row][column] = str(pascal_list[row][column])

    # Get length of the longest number, and set that as the cell_width of the table
    cell_width = len(pascal_list[width - 1][height - 1])

    # Define the string that holds the entire cart
    chart_total = ""

    # Iterate through the rows vertically
    for row in range(height):

        # Set the value of the chart's row to be an empty string
        chart_row = ""

        # Iterates through the columns in the row
        for column in range(width):

            # adds: {p[row][column]:<cell_width}
            chart_row += "{p[" + str(row) + "][" + str(column) + "]:<" + str(cell_width) + "} "

        # Add the formatted chart_row adn a newline to the chart_total
        chart_total += chart_row.format(p = pascal_list) + "\n"

    # Print the entire chart
    print(row_string_total)

# A2
print("\n A2")
print(two23([2, 2]))
print(two23([3, 3]))
print(two23([2]))

# B1
print("\n B2")
print(tenStreak([2, 10, 3, 4, 20, 5]))
print(tenStreak([10, 1, 20, 2]))
print(tenStreak([10, 1, 9, 20]))

# C2
print("\n C2")
print(acromatch(["Chartered","Accountant"], ["Canadian", "Awards"]))
print(acromatch(["United","States", "of", "America"], ["United","Services", "Association"]))
print(acromatch(["Major", "League", "Baseball"], ["Minor", "League", "Baseball"]))

# D2
print("\n D2")
print(canVote("10/12/1995"))
print(canVote("12/01/1998"))
print(canVote("10/31/1998"))

# E2
print("\n E2")
print_pascal(15, 15)

