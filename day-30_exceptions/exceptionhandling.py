#Exception Handling

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:           # If FileNotFoundError do this
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:   # If KeyError do this and save error as a value
    print(f"The key {error_message} does not exist.")
else:                               # Gets executed after try if there are no errors "What else do you want to do"
    content = file.read()
    print(content)
finally:                            # Gets excecuted no matter what at the end
    raise TypeError("This is an error that I made up.")

#BMI Example: Raising own error

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:                      # If height is above 3 meters raise a ValueError with the text
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)