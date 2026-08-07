#Write a program to create, concatenate and print a string and accessing sub-string from a given string.

first_word = "Hello"
second_word = "World I,m Priyanshu Kumar"

full_sentence = first_word + " " + second_word

#  Print the concatenated string
print("Full String:", full_sentence)


sub_string = full_sentence[0:5]
sub_string2 = full_sentence[12:31]

# Print the extracted substring
print("Extracted Substring:", sub_string)
print("Extracted Substring 2:", sub_string2)