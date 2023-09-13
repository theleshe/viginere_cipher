import os

#clears console and prints title of program
def clear_and_print_name():
    os.system('cls||clear')
    print("\t\t-vigenere cipher by theleshe-")

alphabet = {"a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7, "i" : 8, "j" : 9, "k" : 10, "l" : 11, "m" : 12, "n" : 13, "o" : 14, "p" : 15, "q" : 16, "r" : 17, "s" : 18, "t" : 19, "u" : 20, "v" : 21, "w" : 22, "x" : 23, "y" : 24, "z" : 25, " " : 26, "," : 27, "." : 28} 
re_alphabet = {0 : "a", 1 : "b", 2 : "c", 3 : "d", 4 : "e", 5 : "f", 6 : "g", 7 : "h", 8 : "i", 9 : "j", 10 : "k", 11 : "l", 12 : "m", 13 : "n", 14 : "o", 15 : "p", 16 : "q", 17 : "r", 18 : "s" , 19 : "t" , 20 : "u", 21 : "v", 22 : "w", 23 : "x" , 24 : "y" , 25 : "z", 26 : " ", 27 : ",", 28 : "."} 
alphabet_size = 29

clear_and_print_name()

#encrypt or decrypt: method_choose = 1 is encrypt ; method_choose = 2 is decrypt
method_choose = -1
while method_choose != 1 and method_choose != 2 :
    try:
        method_choose = int(input("choose method of algorithm : \n1 - encrypt \n2 - decrypt \n\t"))
    except ValueError:
        print ("\terror(!!!) please, enter a number\n")

clear_and_print_name()

#input_type_choose = 1 is reading file input.txt ; input_type_choose = 2 is keyboard input
input_type_choose = -1
while input_type_choose != 1 and input_type_choose != 2:
    try:
        input_type_choose = int(input("1 - from file input.txt\n2 - keyboard input\n\t"))
    except:
        print("\terror(!!!) please, not text, just number of menu\n")

clear_and_print_name()

#input_text and key input
try:
    if input_type_choose == 1:
        try:
            with open("input.txt", "r") as file:
                input_text = file.readline()
                print("enter source text:\n\t" + input_text)
        except:
            print("\terror(!!!) something with file reading")
    else:
            if method_choose == 1:
                print("enter source text: ")
            else:
                print("enter cipher text: ")
            input_text = input("\t")
    print("enter text key: ")
    key = input("\t")
except ValueError:
        print("\terror(!!!) please, enter text, not numbers or something else\n")
        exit()

if (len(input_text) > 100):
    print("\tsorry, maximum length of input text is 100, no more =)")
    exit()
    
#viginere cipher
try:
    counter = 0
    output_text = ""
    for symbol in input_text:
        inp_symbol_number = alphabet[symbol]
        key_symbol_number = alphabet[key[counter]]
        if method_choose == 1:  #encrypt
            out_symbol_number = (inp_symbol_number + key_symbol_number) % alphabet_size
        else:
            out_symbol_number = (inp_symbol_number - key_symbol_number) #decrypt
            if out_symbol_number < 0:
                out_symbol_number += alphabet_size
        out_symbol = re_alphabet[out_symbol_number]
        output_text += out_symbol

        counter += 1
        counter %= len(key)
except KeyError:
    print("\terror(!!!) there is no such symbol in the alphabet")
    exit()

if method_choose == 1:
    print("cipher text is : \n\t" + output_text)
else:
    print("source text is : \n\t" + output_text)

with open("output.txt", "w") as file:
    file.write(output_text)
