"""
This application will be translating a sentence based on user inputs.
A text file will be read, and then a list of strings will be created within the file.
The captured list is then compared to a dictionary.

We will be defining a function that splits a user's input into a set of strings
A loop will then run through the array of strings and match the word with the translation dictionary.

The full translated set will be print to the user.
"""

"""
main():
    sentence = input()
    dictionary = create_dictionary()
    translate(sentence, dictionary)

translate(sentence, dictionary):
word
each word, translate
print to user

create the dictionary
    read in textese.txt
    create list from each line
    close the file
    create a dict off the new list
    return the dict

main()
"""
def main():
    sentence = input("Enter your sentence: ")
    dictionary = create_dictionary("textese.txt")
    translate(sentence, dictionary)

def create_dictionary(txt_file):
    infile = open(txt_file, "r")
    words = [word.rstrip() for word in infile]
    infile.close()
    return dict([word.split(",") for word in words])

def translate(sentence, dictionary):
    words = sentence.split()
    for word in words:
        print(dictionary.get(word, word), " ", end="")

main()