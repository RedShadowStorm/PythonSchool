# -------------------------------------------------------------------------------
# Name:	    chinese_filter.py
# Purpose:  Convert add a Chinese dialect to an inputted text file(source.txt)
#           and output the dialectized file as output.txt
#
#
# Author:	Me
#
# Created:	February 22, 2013
# -------------------------------------------------------------------------------

source = open("source.txt", "r")

text = source.read()

text_words = text.split(" ")
punctuation = [".", ",", ";"]

for i in range(len(text_words)):
    for j in range(len(text_words[i])):
        if text_words[i][j] in punctuation:
            text_words.insert(i + 1, " Aiyah!")

text = " ".join(text_words)

text_letters = list(text)

for i in range(len(text_letters)):
    try:
        if text_letters[i] == "l":
            text_letters[i] = "r"

        elif text_letters[i] == "L":
            text_letters[i] = "R"

        elif text_letters[i] == "v":
            text_letters[i] = "w"

        elif text_letters[i] == "V":
            text_letters[i] = "W"

        elif text_letters[i] == "t" and text_letters[i + 1] == "h":
            text_letters[i] = "z"
            text_letters.pop(i+1)

        elif text_letters[i] == "T" and text_letters[i + 1] == "h":
            text_letters[i] = "Z"
            text_letters.pop(i+1)

    except IndexError:
        break

text = "".join(text_letters)

print(text_letters)
print(text)

source.close()

translated = open("translated.txt", "w")

translated.write(text)
