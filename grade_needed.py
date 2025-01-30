#initialize by creating variables and gathering user inputs
targetLetterGrade = input("Enter the grade you want in the class: ")
targetPercentageGrade = float(input("Enter the percent you need to get that grade: "))
currentGrade = float(input("Enter your current percent in the class: "))
finalPercentage = float(input("Enter the weight of the final: "))
finalWeight = finalPercentage/100

#calculate needed final exam grade
finalExamGrade = (targetPercentageGrade - currentGrade + finalWeight * currentGrade) / finalWeight

#display needed final exam grade
print(f"You need to get at least {finalExamGrade:.2f}% on the final to get a {targetLetterGrade} in the class.")
