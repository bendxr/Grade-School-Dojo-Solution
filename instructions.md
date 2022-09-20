# Instructions


You're the director of a well-renowned school and you decided to modernize the students classes management.

You have to deal only with 2 types of informations : 
* student's name (only 1 name) : string
* grade (which corresponds to the year level): integer > 0

Basically, you have to manage the school's roster, ie, the students and their associated grade.
Some use cases : 
* Add a student's name to the roster for a grade
  * *"Add Jim to grade 2"*
-> **OK**
* Get a list of all students enrolled in a grade
  * *"Which students are in grade 2 ?"*
-> **Jim**
* Get a sorted list of all students in all grades.
  * Grades should sort as 1, 2, 3, etc., and students within a grade should be sorted alphabetically by name.
  * *"Who all is enrolled in school right now?"*
      * Given that Anna, Barb, and Charlie are in grade 1 ; Alex, Peter, and Zoe in grade 2 ; Jim in grade 5
-> **Anna, Barb, Charlie, Alex, Peter, Zoe, Jim**

Note that :
* all the students only have one name
* when creating a school, you have to define the maximal grade handled by that school (5 by default)
* each student cannot be added more than once to the roster
* you cannot add a student to a grade below 1 or above the maximal grade of the school
* when a student graduate, its grade is increased by 1
* when a student graduate and is already at max grade, he exits from school (he's got his final diploma)


# Implementation guidelines
Your goal is to make all the unit tests pass (don't hesitate to look at their code).

## Exceptions
Don't neglect the exceptions ; they are thoroughly tested in the unit tests.

Put their code into the ``exceptions.py`` file.

Use cases: 
* adding twince the same student to the roster should raise a ``StudentAlreadyAddedException`` exception (which inherits from  ``ValueError``).
* adding a student with an invalid grade (below 1 or above the maximal grade that the school accepts) should raise a ``GradeOutOfRangeException`` exception (which inherits from ``ValueError``).


## Methods
Inspect the main class skeleton (``School``) and implement all the empty methods.

The comments are meants to guide you and help you in the process.

You are **free** to add some *intermediary methods* to *factorize* your code.

