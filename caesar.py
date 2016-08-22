from sys import argv, exit
# print("I know that these are the words the user typed on the command line: ", argv)
from helpers import alphabet_position, rotate_character

def user_input_is_valid(argv):
        for i in argv:               
                if not argv.isdigit():
                # print("usage: python3 caesar.py n")
                # exit()
                return(False)
        
def encrypt(text, rot):
        textlst = list(text)
        for i in range(len(textlst)):
                if textlst[i].isalpha():
                        if textlst[i].isupper():
                                upper = True
                        else:
                                upper = False
                        textlst[i] = rotate_character(textlst[i], rot)
                        if upper == True:
                                textlst[i] = textlst[i].upper()
        return "".join(textlst)
        
# string = input("Enter the text to be encrypted.")
# rot = input("Enter the amount to rotate the text by.")
# print(encrypt(string, rot))
