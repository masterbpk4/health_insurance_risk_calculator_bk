##Brenden Kelley 2020 All Rights Reserved
##Just kidding this is all open source
##Just make sure you credit me if you realize that this is a marvel of coding genius and decide to use it in the future
##This code has been copied from my Matchmaker Python and modified to do the things we want in the new 


##First we need to get our questions placed in an array and ready to be pulled on command, we'll also need an empty array to keep track of the user's score
question = ["Enter the person's age in years: " , "Enter the person's height in inches: " , "Enter the person's weight in pounds: " , "Enter the person's systolic blood pressure: " , "Enter the person's diastolic blood pressure: " , "Does the person have a family history of ... " , "Diabetes? " , "Cancer? " , "Alzheimer's? "]
score = []
bloodpressure = []
height = []
weight = []
familyhistory = []
##We need an introduction to our program
def Intro():
    print("=".center(120, "="))
    print("This program helps you classify health insurance \nbased on their risk level. That is determined \nby their health. Their health is judged in terms \nof their body-mass index, blood pressure, age, \nand family history of disease." )
    print("=".center(120, "="))
##The function that was here was amove to simply be a part of the next function all on it's own, it's also the bulk of the changes that were made to the code.
##Next we need the function to ask the questions to the user, this function also adds to the 'score' array as the answers are obtained.
def askquestions():
    for i in range(0, len(question)):
        k = 0
        while k < 1:
            try:
                j = input(question[i])
                j = j.lower()
                if i == 0:
                    if int(j) >= 0 and int(j) < 30:
                        score.append(0)
                        k = 1
                    elif int(j) >= 30 and int(j) < 45:
                        score.append(10)
                        k = 1
                    elif int(j) >= 45 and int(j) < 60:
                        score.append(20)
                        k = 1
                    elif int(j) >= 60:
                        score.append(30)
                        k = 1
                    else:
                        raise ValueError
                elif i == 1:
                    if int(j) >= 48 and int(j) <= 84:
                        height.append(int(j))
                        k = 1
                    else:
                        raise ValueError
                elif i == 2:
                    if int(j) >= 90:
                        weight.append(int(j))
                        k = 1
                    else:
                        raise ValueError
                elif i == 3 or i == 4:
                    bloodpressure.append(int(j))
                    k = 1
                elif i == 5:
                    k = 1
                    continue
                elif i == 6 or i == 7 or i == 8:
                    if j == "y":
                        familyhistory.append(10)
                        k = 1
                    elif j == "n":
                        familyhistory.append(0)
                        k = 1
                    else:
                        raise ValueError
            except ValueError:
                k = 0
                print("Please enter a valid answer")
        print("=".center(120, "="))
##Now we're going to take all of that data and get a risk score for our patient
def bloodpressurecalc():
    if bloodpressure[0] < 120 and bloodpressure[1] < 80:
        score.append(0)
        print("Blood Pressure: Healthy")
    elif bloodpressure[0] >= 120 and bloodpressure[0] < 130 and bloodpressure[1] < 80:
        score.append(15)
        print("Blood Pressure: Elevated")
    elif bloodpressure[0] >= 130 and bloodpressure[0] < 140 or bloodpressure[1] >= 80 and bloodpressure[1] < 90:
        score.append(30)
        print("Blood Pressure: Stage 1")
    elif bloodpressure[0] >= 140 and bloodpressure[0] < 180 or bloodpressure[1] >= 90 and bloodpressure[1] < 120:
        score.append(75)
        print("Blood Pressure: Stage 2")
    elif bloodpressure[0] >= 180 or bloodpressure[1] > 120:
        score.append(100)
        print("Blood Pressure: Crisis")
def bmicalc():
    heightbmi = height[0] * height[0]
    weightbmi = weight [0]
    bmi = (weightbmi / heightbmi) * 703
    if bmi < 25:
        score.append(0)
        print("BMI: Normal (" + str(bmi) + ")")
    elif bmi >= 25 and bmi < 30:
        score.append(30)
        print("BMI: Overweight (" + str(bmi) + ")")
    elif bmi >= 30:
        score.append(75)
        print("BMI: Obese (" + str(bmi) + ")")
def familyhistorycalc():
    familyscore = familyhistory[0] + familyhistory[1] + familyhistory[2]
    score.append(familyscore)
##And now we need to make the final score
def results():
    total = 0
    for m in range(0, len(score)):
        total = total + score[m]
    if total < 20:
        print("You are at a low risk!")
    elif total >= 20 and total < 50:
        print("You are at a moderate risk!" )
    elif total >= 50 and total < 75:
        print("You are at a high risk!")
    elif total >=75:
        print("You are uninsurable!")
##Now it's time to put everything we've done to work
def dothething():
    Intro()
    input("Press any key to continue...")
    askquestions()
    bloodpressurecalc()
    bmicalc()
    familyhistorycalc()
    results()
    areyoudone()
def areyoudone():
    q = input("Do you have another patient? ")
    if q == "y":
        score = []
        bloodpressure = []
        height = []
        weight = []
        familyhistory = []
        dothething()
    elif q == "n":
        print("All done!")

dothething()