# GPA Calculator (Python)

A simple Python-based GPA/SGPA Calculator that allows users to calculate their semester GPA based on subject credits and marks.

## Features

* Supports both theory and practical subjects
* Accepts subject-wise credits
* Calculates GPA for each subject
* Calculates overall SGPA
* Displays total marks obtained
* Beginner-friendly Python project

## How It Works

### Practical Subjects

The program takes:

* Lab Marks
* Viva Marks

Total marks are calculated out of 100 and converted into GPA according to the grading criteria.

### Theory Subjects

The program takes:

* Internal Marks
* Mid Semester Marks
* End Semester Marks

The End Semester marks are converted according to the university pattern:

Total Marks = Internal + Midsem + (Endsem / 2)

The final marks are then converted into GPA.

## GPA Criteria

| Marks    | GPA |
| -------- | --- |
| 80 - 100 | 10  |
| 70 - 79  | 9   |
| 60 - 69  | 8   |
| 50 - 59  | 7   |
| 40 - 49  | 6   |
| 30 - 39  | 5   |
| 20 - 29  | 4   |
| 10 - 19  | 3   |
| Below 10 | 2   |

## Formula Used

Subject Grade Points:

GPA × Credits

Semester GPA:

SGPA = Total Grade Points / Total Credits

## Example Output

Enter the number of subjects: 3

Enter the name of the subject: Mathematics
Enter the credits of the subject: 4
Subject is practical or not? (y/n): n

...

You scored 8.75 SGPA with 235/300 marks!

## Technologies Used

* Python 3

## Future Improvements

* GUI version using Tkinter
* Grade sheet generation
* Data storage using JSON
* CGPA calculation across multiple semesters
* Error handling for invalid inputs

## Author

Created by a Computer Science student who loves building Python projects and learning Data Structures & Algorithms.
