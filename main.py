total_subjects = int(input("\nEnter the number of subjects: "))

subject = []
maxcredits = []
maxmarks = []
marks = []
gpa = []

for i in range(total_subjects):
    subjectname = input("\n\nEnter the name of the subject: ")
    creditssubject = int(input("Enter the credits of the subject: "))
    ispractical = input("Subject is practical or not? (y/n): ")

    if ispractical == "y":
        labmarks = int(input("Enter lab marks of the subject: "))
        vivamarks = int(input("Enter viva marks of the subject: "))

        totalmarks = labmarks + vivamarks

        if totalmarks >= 80:
            lgpa = 10

        elif totalmarks >= 70:
            lgpa = 9

        elif totalmarks >= 60:
            lgpa = 8

        elif totalmarks >= 50:
            lgpa = 7

        elif totalmarks >= 40:
            lgpa = 6

        elif totalmarks >= 30:
            lgpa = 5

        elif totalmarks >= 20:
            lgpa = 4

        elif totalmarks >= 10:
            lgpa = 3

        else:
            lgpa = 2

        subject.append(subjectname)
        marks.append(totalmarks)
        finalgpa = lgpa*creditssubject
        gpa.append(finalgpa)
        maxmarks.append(100)
        maxcredits.append(creditssubject)

        print(f"\nScored {lgpa}GPA is {subjectname} with {totalmarks} marks")

    else:
        internnalmarks = int(input("Enter the internals of the subject: "))
        midsemmarks = int(input("Enter the midsem of the subject: "))
        endsmarks = int(input("Enter the endsem of the subject: "))

        cendsemmakrs = endsmarks/2
    
        totalmarks = internnalmarks + midsemmarks + cendsemmakrs

        if totalmarks >= 80:
            lgpa = 10

        elif totalmarks >= 70:
            lgpa = 9

        elif totalmarks >= 60:
            lgpa = 8

        elif totalmarks >= 50:
            lgpa = 7

        elif totalmarks >= 40:
            lgpa = 6

        elif totalmarks >= 30:
            lgpa = 5

        elif totalmarks >= 20:
            lgpa = 4

        elif totalmarks >= 10:
            lgpa = 3

        else:
            lgpa = 2

        subject.append(subjectname)
        marks.append(totalmarks)
        finalgpa = lgpa*creditssubject
        gpa.append(finalgpa)
        maxmarks.append(100)
        maxcredits.append(creditssubject)

        print(f"\nScored {lgpa}GPA is {subjectname} with {totalmarks} marks")

totalmarksscored = sum(marks)
totalgpascored = sum(gpa)
maximummarks = sum(maxmarks)
maximumcredits = sum(maxcredits)

final = totalgpascored/maximumcredits

print(f"You scored {final}SGPA with {totalmarksscored}/{maximummarks} marks!")