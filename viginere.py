import os

def clear_and_print_name():
    os.system('cls||clear')
    print("\t\t-vigenere cipher by theleshe-")

#alphabets
alphabet = {"a" : 0, "b" : 1, "c" : 2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7, "i" : 8, "j" : 9, "k" : 10, "l" : 11, "m" : 12, "n" : 13, "o" : 14, "p" : 15, "q" : 16, "r" : 17, "s" : 18, "t" : 19, "u" : 20, "v" : 21, "w" : 22, "x" : 23, "y" : 24, "z" : 25, " " : 26, "," : 27, "." : 28} 
re_alphabet = {0 : "a", 1 : "b", 2 : "c", 3 : "d", 4 : "e", 5 : "f", 6 : "g", 7 : "h", 8 : "i", 9 : "j", 10 : "k", 11 : "l", 12 : "m", 13 : "n", 14 : "o", 15 : "p", 16 : "q", 17 : "r", 18 : "s" , 19 : "t" , 20 : "u", 21 : "v", 22 : "w", 23 : "x" , 24 : "y" , 25 : "z", 26 : " ", 27 : ",", 28 : "."} 
alphabet_size = 29

ru_alphabet = {"а" : 0, "б" : 1, "в" : 2, "г" : 3, "д" : 4, "е" : 5, "ё" : 6, "з" : 7, "и" : 8, "й" : 9, "к" : 10, "л" : 11, "м" : 12, "н" : 13, "о" : 14, "п" : 15, "р" : 16, "с" : 17, "т" : 18, "у" : 19, "ф" : 20, "х" : 21, "ц" : 22, "ч" : 23, "ш" : 24, "щ" : 25, "ъ" : 26, "ы" : 27, "ь" : 28, "э" : 29, "ю" : 30, "я" : 31, " " : 32, "," : 33, "." : 34}
ru_re_alphabet = {0 : "а",1 : "б", 2 : "в",3 : "г",4 : "д", 5 : "е",6 : "ё", 7 : "з", 8 : "и", 9 : "й", 10 : "к", 11 : "л", 12 : "м", 13 : "н", 14 : "о", 15 : "п", 16 : "р", 17 : "с", 18 : "т",19 : "у",20 : "ф", 21 : "х", 22 : "ц", 23 : "ч", 24 : "ш", 25 : "щ", 26 : "ъ", 27 : "ы", 28 : "ь", 29 : "э", 30 : "ю", 31 : "я", 32 : " ", 33 : ",", 34 : "." }
ru_alphabet_size = 35

clear_and_print_name()

#select language
en_language = -1
while en_language != 1 and en_language != 2:
    try:
        en_language = int(input("choose language : \n1 - english\n2 - russian\n\t"))
    except:
        print("\terror(!!!) please, not text, just number of menu")

clear_and_print_name()

#select method
method_choose = -1
while method_choose != 1 and method_choose != 2 :
    try:
        if en_language == 1:
            method_choose = int(input("choose method of algorithm : \n1 - encrypt \n2 - decrypt \n\t"))
        else:
            method_choose = int(input("выберите метод : \n1 - шифровать \n2 - дешифровать \n\t"))
    except ValueError:
        print ("\terror(!!!) please, enter a number\n")

clear_and_print_name()

#select input method
input_type_choose = -1
while input_type_choose != 1 and input_type_choose != 2:
    try:
        if en_language == 1:
            input_type_choose = int(input("1 - from file input.txt\n2 - keyboard input\n\t"))
        else:
            input_type_choose = int(input("1 - читать из файла input.txt\n2 - ввод с клавиатуры\n\t"))
    except:
        print("\terror(!!!) please, not text, just number of menu\n")

clear_and_print_name()

#input
try:
    if input_type_choose == 1:
        try:
            with open("input.txt", "r") as file:
                input_text = file.readline()
                if en_language == 1:
                    print("enter source text:\n\t" + input_text)
                else:
                    print("введите исходный текст:\n\t" + input_text) 
        except:
            print("\terror(!!!) something with file reading")
    else:
            if method_choose == 1:
                if en_language == 1:
                    print("enter source text: ")
                else:
                    print("введите исходный текст: ")
            else:
                if en_language == 1:
                    print("enter cipher text: ")
                else:
                    print("введите шифртекст: ")
            input_text = input("\t")
    if en_language == 1:
        print("enter text key: ")
    else:
        print("введите ключ: ")
    key = input("\t")
except ValueError:
        print("\terror(!!!) please, enter text, not numbers or something else\n")
        exit()

if (len(input_text) > 100):
    print("\tsorry, maximum length of input text is 100, no more =)")
    exit()

#viginere algorithm 
try:
    counter = 0
    output_text = ""
    if en_language == 1:
        for symbol in input_text:
            inp_symbol_number = alphabet[symbol.lower()]
            key_symbol_number = alphabet[key[counter]]
            if method_choose == 1:
                out_symbol_number = (inp_symbol_number + key_symbol_number) % alphabet_size
            else:
                out_symbol_number = (inp_symbol_number - key_symbol_number)
                if out_symbol_number < 0:
                    out_symbol_number += alphabet_size
            out_symbol = re_alphabet[out_symbol_number]
            output_text += out_symbol

            counter += 1
            counter %= len(key)
    else:
      for symbol in input_text:
            inp_symbol_number = ru_alphabet[symbol.lower()]
            key_symbol_number = ru_alphabet[key[counter]]
            if method_choose == 1:
                out_symbol_number = (inp_symbol_number + key_symbol_number) % ru_alphabet_size
            else:
                out_symbol_number = (inp_symbol_number - key_symbol_number)
                if out_symbol_number < 0:
                    out_symbol_number += ru_alphabet_size
            out_symbol = ru_re_alphabet[out_symbol_number]
            output_text += out_symbol

            counter += 1
            counter %= len(key)  
except KeyError:
    print("\terror(!!!) there is no such symbol in the alphabet")
    exit()

#output
if method_choose == 1:
    if en_language == 1:
        print("cipher text is : \n\t" + output_text)
    else:
        print("шифротекст : \n\t" + output_text)
else:
    if en_language == 1:
        print("source text is : \n\t" + output_text)
    else:
        print("исходный текст: \n\t" + output_text)

#write
with open("output.txt", "w") as file:
    file.write(output_text)