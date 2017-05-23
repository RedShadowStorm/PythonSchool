# -------------------------------------------------------------------------------
# Name:	    1337.py
# Purpose:  Converts source.txt into a 1337 dialect, and outputs it to translated.txt
#
#
# Author:	Me
#
# Created:	February 22, 2013
# -------------------------------------------------------------------------------

def convert_letters(text_list, index, input, output):
    """
    This function checks if a certain input is within a list of letters, then it checks whether a string of characters
    of any length is in that list, and if it is, it replaces that string by inserting the desired output into that list
    :param text_list: The list of letters derived from a text file that will have certain latters replaced
    :param index: The current index within text_list
    :param input: The type of text that we want to convert into output
    :param output: The desired text
    """

    # Define variables
    input_length = len(input)
    output_length = len(output)

    # Check if the current index matches the input
    for i in range(input_length):
        if text_list[index+i] != input[i]:
            return

    # Since we didn't return in the previous function
    for i in range(input_length):
        text_list.pop(index)

    # Insert the output in the place of the input that we removed:
    for i in range(output_length):
        text_list.insert(index + i, output[i])

# Open source.txt, read it and define the text variable with that variable
source = open("source.txt", "r")
text = source.read()

# Close source.txt
source.close()

# Convert text into a list of individual characters
text_list = list(text)

# Define a letter bank that has letters and their conversions
alphabet_input  = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet_output = ["@","13","c","d","3","f","6","h","i","J","k","1","m","n","0","p","9","r","5","7","u","v","w","x","y","2"]

# Make a while loop
index = 0

# The while loop iterates through the text as the index increases, until it is greater than or equal to the length of the text
while index <= len(text_list) - 1:

    # Convert input letters in the word bank to their correspinding outputs
    for i in range(len(alphabet_input)):
        convert_letters(text_list, index, alphabet_input[i], alphabet_output[i])

    # Convert input words into their corresponding translations
    convert_letters(text_list, index, "hacks", "hax")
    convert_letters(text_list, index, "sucks", "sux")
    convert_letters(text_list, index, "owned", "pwned")
    convert_letters(text_list, index, "banned", "b&")

    # Convert input phrases into their corresponding translations
    convert_letters(text_list, index, ". ", ". I'm gunna DDOS u n00b!!!!")

    # Increment index
    index += 1


# Give the text the new value of the new formatted list of letters
text = "".join(text_list)

# Open the translated file and write text to that file
translated = open("translated.txt", "w")
translated.write(text)



