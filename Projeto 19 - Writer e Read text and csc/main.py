#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
from Demos.SystemParametersInfo import y

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt", "r") as letter:
    linha_starting = letter.read()

    with open("./Input/Names/invited_names.txt", "r") as list_names:
        #print(list_names)

        for name in list_names:
            name = name.strip()
            #print(name)
            linha_update = linha_starting.replace("[name]", f"{name}")
            #print(linha_update)

            with open(f"./Output/ReadyToSend/Carta_para_{name}.txt", "w") as new_letter:
                new_letter.write(linha_update)
