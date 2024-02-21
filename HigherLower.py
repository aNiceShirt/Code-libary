import HigherLowerArt
import HigherLowerGameData
import random

logo = HigherLowerArt.logo
vs = HigherLowerArt.vs
data = HigherLowerGameData.data

# Generate two random persons with randint()
def GeneratePerson():
    PersonNum = random.randint(0,len(data)-1)
    PersonDetails = data[PersonNum]
    return PersonDetails

def Highest(PersonA, PersonB):
    highest = ""
    if PersonA > PersonB:
        highest = "A"
    else:
        highest = "B"
    return highest


def HigherLower():
    PersonA = GeneratePerson()
    score = 0
    lost = False
    while lost != True:
        PersonB = GeneratePerson()
        while PersonB == PersonA:
            PersonB = GeneratePerson()
        highest = Highest(int(PersonA.get('follower_count')), int(PersonB.get('follower_count')))
        print(logo)
        print(f"Score {score}")
        # Print comparison
        print(f"Compare A: {PersonA.get('name')}, a {PersonA.get('description')} from {PersonA.get('country')}.")
        print(vs)
        print(f"Against B: {PersonB.get('name')}, a {PersonB.get('description')} from {PersonB.get('country')}.")

        # Ask user for higher or lower input(A/B:?).lower()
        UserChoice = input("Who has more followers A or B? ").upper()

        if UserChoice == highest:
            print("You win")
            score += 1
            print(f"Score: {score}")
            PersonA = PersonB
        else:
            print("You lost")
            print(f"{PersonA.get('name')} has {PersonA.get('follower_count')} million followers and {PersonB.get('name')} has {PersonB.get('follower_count')} million followers")
            print(f"Final score: {score}")
            lost = True

HigherLower()

PlayAgain = input("Play again? (y/n): ").lower()
if PlayAgain == "y":
    HigherLower()