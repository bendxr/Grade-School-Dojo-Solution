from exceptions import *

class School:
                
    def __init__(self, max_grade=5):
      """
      Parameters
      ----------
      max_grade : integer
        Maximal grade handled by the school
      """
      self.students = {}
      if max_grade < 1:
        raise GradeOutOfRangeException("Grade must not be lower than 1")
      else:
        self.max_grade = max_grade

    def __is_grade_valid(self, grade):
        if (grade < 1): 
          raise GradeOutOfRangeException("Grade must not be lower than 1")
        if (grade > self.max_grade):
          raise GradeOutOfRangeException("Grade must not be greater than {}".format(self.max_grade))
  
    def add_student(self, name, grade):
      """
      Parameters
      ----------
      name : string
          Name of the student to add in the school.
      grade : int
          grade of the student to add in the school.
      Returns
      -------
      dict
          Updated dict (key = name, value = grade) with the new student linked to it's grade
      """
      self.__is_grade_valid(grade)
      if name not in self.students.keys():
        return self.students.update({name : grade})
      else:
        raise StudentAlreadyAddedException(f"{name} already in the roster")

    def roster(self):
        """
        Returns
        -------
        roster : list
            list of all students names ordered by grade then by alphabetical order.
        """
        return [name for grade_number in sorted(set(self.students.values())) for name in self.grade(grade_number)]

  
    def roster_grades(self):
      """
      Returns
      -------
      roster : list
          list of all students names ordered by grade then by alphabetical order.
      Challenge
      ---------
      Try to find the 1-line implementation !
      """
      res = ""
      for name in self.roster():
          res = res + name + " : " + str(self.students.get(name)) + "\n"
      return res

    def roster_names(self):
      """
      Returns
      -------
      register with grade: string
          roster with only comma+space-separated names informations
          e.g: "alice, bob, charlie"
      """
      res = ""
      r = self.roster()
      if len(r) > 0:
        res = r[0]
        for i in range(1, len(r)):
          res = res + ", " + r[i]
      return res
      
  
    def grade(self, grade_number):
      """
      Parameters
      ----------
      grade_number : int
          grade of which we want the students in 
      Returns
      -------
      list
          names of the students in this grade ordered by alphabetical order.
      Challenge
      ---------
      Try to find the (almost) 1-line implementation !
      """
      self.__is_grade_valid(grade_number)
      return sorted([name for name,grade in self.students.items() if grade == grade_number])

    def is_added(self, name):
      """
      Returns
      -------
      added status : boolean
          true if name has already been added to the roster, false otherwise
      """
      return name in self.students.keys();

    def graduate(self, name):
      """
      Parameters
      ----------
      name : str
          name of student that pass to the next grade or exit school if cursus is finished
      """
      
      g = self.students[name]
      if (g < self.max_grade):
        self.students.update({ name : g + 1 })
      else:
        self.students.pop(name)

    def graduate_class(self, grade_number):
      """
      Parameters:
      -----------
      grade_number: int
          grade of the class that will graduate (pass to the next grade) or exit school if cursus is finished
      Challenge
      ---------
      Try to find the 1-line implementation !
      """
      self.students = { k:v+1 if (v == grade_number) else v for k,v in self.students.items() if v < self.max_grade }
        
    def close(self):
      """
      Closes the school : removes all the students from roster      
      """
      self.students.clear()