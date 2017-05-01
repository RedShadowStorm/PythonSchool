# two23
# A function that checks if there are at least 2 occurences
def two23(num_list):
    # Define the number of occurences of 2 and the number of occurences of 3 in the list
    num_2 = 0
    num_3 = 0

    for num in num_list:
        if num == 2:
            num_2 += 1
        elif num == 3:
            num_3 += 1

    return num_2 >= 2 or num_3 >= 3

def tenStreak(num_list):

    multiple = 0
    seen_multiple = False

    for i in range(len(num_list)):

        if num_list[i]%10 == 0:
            multiple = num_list[i]
            seen_multiple = True

        elif seen_multiple:
            num_list[i] = multiple

    return num_list

def acromatch(acronym_1, acronym_2):

    if len(acronym_1) == len(acronym_2):
        for i in range(len(acronym_1)):
            if acronym_1[i][1] != acronym_2[i][1]:
                return False

    return True

def canVote(birth):

    youngest_month, youngest_day, youngest_year = [11, 8, 1998]

    birth_list = birth.split("/")

    for i in range(3):
        birth_list[i] = int(birth_list[i])

    birth_month, birth_day, birth_year = birth_list

    if birth_year < youngest_year:
        return True

    elif birth_month < youngest_month and birth_year == youngest_year :
        return True

    elif birth_day <= youngest_day and birth_month == youngest_month:
        return True

    else:
        return False


def pascal(width, height):

    # Create table filled with the number 1
    pascal_list = [[1 for column in range(width)] for row in range(height)]

    for row in range(1,height):
        for column in range(1, width):
            pascal_list[row][column] = (pascal_list[row -1][column]) + (pascal_list[row][column - 1])

    # Convert all of it to strings
    for row in range(height):
        for column in range(width):
            pascal_list[row][column] = str(pascal_list[row][column])

    row_string_total = ""

    for row in range(height):
        row_string = ""
        for column in range(width):
            row_string += "{p[" + str(row) + "][" + str(column) + "]:<4}" + " "

        row_string_total += row_string.format(p = pascal_list) + "\n"

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
pascal(10, 10)

