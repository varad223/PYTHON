class Employee:
        totalempoyee = 0
        males = 0
        females = 0



        def __inti__(self,name,designation,gender,doj,salary):
              self.name=name
              self.designation=designation
              self.gender=gender
              self.doj=doj
              self.salary=salary
              Employee.toatlemployee +=1
              if self.gender=='M':
                      Employee.males +=1
              else:
                      Employee.females +=1


        def totalemployeeCount ():
                return Employee.totalEmployee

        def gendercount():
               print('males:',Employee.males)
               print('females:',Employee.females)


        def isAsstManager(self):
               if self.designation == "Asst Manager":
                       return true
               else:
                       return false



def create():
        name=input("name")
        designation=input("Designation")
        gender=input("Gender(M/F):")


        doj=input('enter a date of joining')
        salary=int(input("salary:"))
        emp = Employee(name,designation,gender,doj,salary)
        return emp


emp_list =[]
while(1):

        print("1.creat Employee\n2.Total Employee\n3.Gender count\n4.Employee with salary>10000\n5.Employee with designation Asst maneger")


        choice = int(input("enteryour chois:"))
        if choice ==1:
                emp_list.append(create())
        elif choice ==2:
                print("total employee:",employee.totalemployeecount())
        elif choice ==3:
                print(employee.gendercount())
        elif choice ==4:
                for emp in epm_list:
                        if emp.isSalaryGreter10000():
                                 print("Employee having salary > 10000 is:",emp.name)


        elif choice ==5:
                 for emp in emp_list:
                         if emp.isAsstManager():
                                  print("Employee with designation Asst Manager is :",emp.name)
        else:
                    print("invalid choice")
                    exit() 
