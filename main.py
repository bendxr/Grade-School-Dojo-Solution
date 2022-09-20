from grade_school import School
from exceptions import StudentAlreadyAddedException

school = School(4)

school.add_student('joe', 1)
school.add_student('claire', 2)
school.add_student('zoe', 2)
school.add_student('charlotte', 2)
list = school.roster()
print("list = {}".format(list))
s = school.grade(2)
print("s = {}".format(s))
try:
  school.add_student('claire', 1)
except StudentAlreadyAddedException as ex:
  print("Failure: {}".format(ex.message))
try:
  school.add_student('claire', 2)
except StudentAlreadyAddedException as ex:
  print("Failure: {}".format(ex.message))
isadded = school.is_added('claire')
print("is_added = {}".format(isadded))

print("{}".format(school.roster_grades()))
print("{}".format(school.roster_names()))
school.graduate('claire')
print("{}".format(school.roster_grades()))
print("{}".format(school.roster_grades()))
print("{}".format(school.roster_grades()))

school.add_student('adam', 3)
print("{}".format(school.roster_grades()))

school.graduate_class(4)
print("{}".format(school.roster_grades()))

school.close()
print("AFTER close")
print("{}".format(school.roster_grades()))
