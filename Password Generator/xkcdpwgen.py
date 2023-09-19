import sys
import random
from random import randrange

words = 4
caps = 0
numbers = 0
symbols = 0
password = []

for i, arg in enumerate(sys.argv):
    if (arg == "-w") or (arg == "--words"):
        try:
            words = sys.argv[i + i]
            if not words.isdigit():
                raise Exception()
        except:
            sys.exit("invalid input")
    elif (arg == "-c") or (arg == "--caps"): 
        try:
            caps = sys.argv[i + 1]
            if (not caps.isdigit()) or (int(caps) > int(words)): 
                raise Exception()
        except:
            sys.exit("invalid input")
    elif (arg == "-n") or (arg == "--numbers"): 
        try: 
             numbers = sys.argv[i + 1] 
             if not numbers.isdigit(): 
                raise Exception() 
        except: 
             sys.exit("invalid input") 
    elif (arg == "-s") or (arg == "--symbols"): 
        try: 
             symbols = sys.argv[i + 1] 
             if not symbols.isdigit(): 
                 raise Exception() 
        except: 
             sys.exit("invalid input") 
    elif (arg == "-h") or (arg == "--help"):
        print("usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]\n\n" +
              "optional arguments:\n" + 
              "-h, --help            show this help message and exit\n" +
              "-w WORDS, --words WORDS\n" + 
              "                      include WORDS words in the password (default=4)\n" +
              "-c CAPS, --caps CAPS  capitalize the first letter of CAPS random words\n" +
              "                      (default=0)\n" +
              "-n NUMBERS, --numbers NUMBERS\n" +
              "                      insert NUMBERS random numbers in the password\n" +
              "                      (default=0)\n" +
              "-s SYMBOLS, --symbols SYMBOLS\n" + 
              "                      insert SYMBOLS random symbols in the password\n" +
              "                      (default=0)\n")
            
def word():
    file = open('words.txt')
    content = file.readlines()
    return content[random.randint(0, len(content))].strip()

for n in range(int(words)): 
    password.append(words) 
caps_list = random.sample(range(int(words)), int(caps)) 

for n in caps_list: 
    password[n] = password[n].capitalize() 

nums_list = random.sample(range(int(words)*2), int(numbers)) 

for n in nums_list: 

     if n < int(words): 
        password[n] = str(randrange(10)) + password[n] 

     else: 

         password[n - int(words)] = password[n - int(words)] + str(randrange(10)) 

symb_list = random.sample(range(int(words)*2), int(symbols)) 

symb = ["~", "!", "@", "#", "$", "%", "^", "&", "*", ".", ":", ";"] 

for n in symb_list: 

     if n < int(words): 

         password[n] = symb[randrange(12)] + password[n] 

     else: 

         password[n - int(words)] = password[n - int(words)] + symb[randrange(12)] 

this = ""

for n in password:
    this += n