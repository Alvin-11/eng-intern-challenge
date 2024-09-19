
def main():
 import sys
 def braille_to_english(input):
    alphabet_braille ={
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e",
    "OOO...": "f", "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j",
    "O...O.": "k", "O.O.O.": "l", "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o",
    "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r", ".OO.O.": "s", ".OOOO.": "t",
    "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x", "OO.OOO": "y",
    "O..OOO": "z", "......": " ",
    "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!",
    "..OO..": ":", "..O.O.": ";", "....OO": "-", ".O..O.": "/",
    ".OO..OO": "<", "O..OO.": ">", "O.O..O": "(", ".O.OO.": ")",
    ".....O": "capital", ".O.OOO": "number", ".O.OOO": "decimal"}
    number_braille = {
    "......": " ",
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5",
    "OOO...": "6", "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0",
    "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!",
    "..OO..": ":", "..O.O.": ";", "....OO": "-", ".O..O.": "/",
    ".OO..OO": "<", "O..OO.": ">", "O.O..O": "(", ".O.OO.": ")",
    ".....O": "capital", ".O.OOO": "number", ".O.OOO": "decimal"
}
    output = ""
    i = 0
    while i < len(input):
        numbers = False
        braille = input[i:i+6]
        if braille == alphabet_braille[" "]:
           numbers = False
        if alphabet_braille["capital"] == braille:
            output = alphabet_braille[braille].upper()
            i+=1
        elif alphabet_braille["number"] == braille and numbers == False:
            output = number_braille [braille]
            i+=1
           
        else:
            output = alphabet_braille[braille]
        i += 1
    print(output)
   
 def english_to_braille(input):
   braille_alphabet = { 
    "a": "O.....", "b": "O.O...", "c": "OO....", "d": "OO.O..", "e": "O..O..",
    "f": "OOO...", "g": "OOOO..", "h": "O.OO..", "i": ".OO...", "j": ".OOO..",
    "k": "O...O.", "l": "O.O.O.", "m": "OO..O.", "n": "OO.OO.", "o": "O..OO.",
    "p": "OOO.O.", "q": "OOOOO.", "r": "O.OOO.", "s": ".OO.O.", "t": ".OOOO.",
    "u": "O...OO", "v": "O.O.OO", "w": ".OOO.O", "x": "OO..OO", "y": "OO.OOO",
    "z": "O..OOO", " ": "......",

    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.",
    ":": "..OO..", ";": "..O.O.", "-": "....OO", "/": ".O..O.",
    "<": ".OO..OO", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO.",

    "capital": ".....O", "number": ".O.OOO", "decimal": ".O.OOO"}
   braille_number = { 

    "1": "O.....", "2": "O.O...", "3": "OO....", "4": "OO.O..", "5": "O..O..",
    "6": "OOO...", "7": "OOOO..", "8": "O.OO..", "9": ".OO...", "0": ".OOO..",

    ".": "..OO.O", ",": "..O...", "?": "..O.OO", "!": "..OOO.",
    ":": "..OO..", ";": "..O.O.", "-": "....OO", "/": ".O..O.",
    "<": ".OO..OO", ">": "O..OO.", "(": "O.O..O", ")": ".O.OO.",

    "capital": ".....O", "number": ".O.OOO", "decimal": ".O.OOO"}
   output = ""
   numbers = False
   for char in input:
        
        if char ==  braille_alphabet[" "]:
           numbers = False
        if char.isupper():
            output += braille_alphabet["capital"]  # Capital letter indicator
            output += braille_alphabet[char.lower()]
        elif char.isdigit() and numbers == False:
            output += braille_alphabet["number"]  # Capital letter indicator
            output += braille_number[char]
            numbers = True
        elif char.isdigit():
            output += braille_number[char]
        else:
            output += braille_alphabet[char]
   print(output)

 def translate_decider(input):
   
   for i in range(len(input)):
    if input[i]!="." or input[i]!="O" :
       english_to_braille(input)
       return
   braille_to_english(input)
   return
     
 userInput = input()
 translate_decider(userInput)
 sys.exit()



if __name__ == "__main__": # main area where the entire program is run

   try:
      while True:
         main()
   except Exception as e: # exception handling
      print("An error has occured")
