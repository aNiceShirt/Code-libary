#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("J:/Google Drive/Coding/Python/100Days of Code Python/Code libary/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") as starting_letter:
                starting_letter = starting_letter.readlines()

with open("J:/Google Drive/Coding/Python/100Days of Code Python/Code libary/Mail Merge Project Start/Input/Names/invited_names.txt", mode="r") as invited_names:
                invited_names_list = invited_names.readlines()

names = []
for name in invited_names_list:
    stripped_name = name.strip()
    names.append(stripped_name)


for name in names:
    new_letter = starting_letter[0].replace("[name]", name)
    with open(f"J:/Google Drive/Coding/Python/100Days of Code Python/Code libary/Mail Merge Project Start/Output/ReadyToSend/{name}.txt", mode="w") as f:
         f.write(new_letter)
         for list in range(1,len(starting_letter)):
               f.write(starting_letter[list])   
         
            
    
