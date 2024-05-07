import os

morse = {"a":".-" , "b":"-..." , "c" : "-.-." , "d" : "-.." , "e" : "." , "f" : "..-." ,
         "g":"--." , "h":"....","i":".." , "j":".---" , "k" : "-.-" ,"l":".-.." , "m":"--" , "n":"-.",
         "o":"---","p":".--.","q":"--.-","r":".-.","s":"..." , "t":"-" , "u":"..-" , "v":"...-",
         "w":".--","x":"-..-","y":"-.--" , "z":"--.." , " " : "" , "1":".----","2":"..---","3":"...--","4":"....-","5":".....",
         "6":"-....","7":"--...","8":"---..","9":"----.","0":"-----"}

def textToMorse(name):
    name = name.lower()
    name = list(name)
    for i in name:
        m = list(morse[i])
        for j in m:
            print(j, end="")
        print("/" , end="")
        
def morseToText(text):
    key = list(morse.keys())
    value = list(morse.values())
    text = text.split("/")
    for i in text:
        print(key[value.index(i)],end="")
    print(" ")
    
def main():
    options = ["1. From Morse to text" , "2. From Text to Morse"]
    for i in options:
        print(i)

    choice = int(input("Enter your choice : "))
    if choice == 1:
        morseCode = str(input("Enter your morse code (Put / between charachetrs and // between words) : "))
        morseToText(morseCode)
    elif choice == 2:
        text = str(input("Enter the text you want to translate : "))
        textToMorse(text)
    else:
        os.system("cls")
        main()

main()