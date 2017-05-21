# -------------------------------------------------------------------------------
# Name:	    1337.py
# Purpose:  Convert add a Chinese dialect to an inputted text file(source.txt)
#           and output the dialectized file as output.txt
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
        if text_list[index + i] != input[i]:
            return

    # Since we didn't return in the previous function
    for i in range(input_length):
        text_list.pop(index)

    # Insert the output in the place of the input that we removed:
    for i in range(output_length):
        text_list.insert(index + i, output[i])

source = open("source.txt", "r")

text = source.read()

text_list = list(text)

alphabet_original   = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet_translated = ["@","8","c","d","3","f","g","h","i","J","k","1","m","n","0","p","9","r","s","7","u","v","w","x","y","z"]

index = 0
while index <= len(text_list) - 1:
    convert_letters(text_list, index, ". ", ". I'm gonna DDOS u!!!!")

    for i in range(len(alphabet_original)):
        convert_letters(text_list, index, alphabet_original[i], alphabet_translated[i])

    index += 1

source.close()

text = "".join(text_list)

translated = open("translated.txt", "w")
translated.write(text)



