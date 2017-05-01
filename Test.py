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

pascal(20, 30)
