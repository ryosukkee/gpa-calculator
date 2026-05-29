lookup_table = [
    (80, 10),
    (70, 9),
    (60, 8),
    (50, 7),
    (40, 6),
    (30, 5),
    (20, 4),
    (10, 3),
    (0, 2)
]

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

        for cutoff, grade in lookup_table:
            if totalmarks >= cutoff:
                lgpa = grade
                break

        subject.append(subjectname)
        marks.append(totalmarks)

        finalgpa = lgpa * creditssubject
        gpa.append(finalgpa)

        maxmarks.append(100)
        maxcredits.append(creditssubject)

        print(f"\nScored {lgpa} GPA in {subjectname} with {totalmarks} marks")

    else:

        internnalmarks = int(input("Enter the internals of the subject: "))
        midsemmarks = int(input("Enter the midsem of the subject: "))
        endsmarks = int(input("Enter the endsem of the subject: "))

        cendsemmarks = endsmarks / 2

        totalmarks = internnalmarks + midsemmarks + cendsemmarks

        for cutoff, grade in lookup_table:
            if totalmarks >= cutoff:
                lgpa = grade
                break

        subject.append(subjectname)
        marks.append(totalmarks)

        finalgpa = lgpa * creditssubject
        gpa.append(finalgpa)

        maxmarks.append(100)
        maxcredits.append(creditssubject)

        print(f"\nScored {lgpa} GPA in {subjectname} with {totalmarks} marks")

totalmarksscored = sum(marks)
totalgpascored = sum(gpa)

maximummarks = sum(maxmarks)
maximumcredits = sum(maxcredits)

final = totalgpascored / maximumcredits

print("\n" + "=" * 40)
print("SEMESTER RESULT")
print("=" * 40)

for i in range(len(subject)):
    print(f"{subject[i]} : {marks[i]}/100")

print(f"\nTotal Marks : {totalmarksscored}/{maximummarks}")
print(f"SGPA        : {final:.2f}")