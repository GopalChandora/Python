'''
ACCESS MODIFIERS

1 .public : use simple variable 
        example : var = 10 
2 .protected : use single underscore ( _ ) before variable name
        example: _var = 10
3. private :  use double underscore  ( __ ) before variable name
        example : __var = 10
'''

class School:
    PeonSalary = 5000
    _TeacherSalary = 10000
    __PrincipalSalary = 15000

sc = School()
print("Peon Salary = ",sc.PeonSalary) #Public Variable accessing (object.variableName)
print("Teacher Salary = ",sc._TeacherSalary) #Protected Variable accessing (object._variableName)
print("Principal Salary"+sc._School__PrincipalSalary) #Private Variable accessing (object._className__variableName)