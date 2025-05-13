class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
        
    def __str__(self):
        return "First Name: " + str(self.firstname) + "\nLast Name: " +str(self.lastname)
    # f is to format string
    # \n is for new line 
    #Overloading the print function



    ##Add operator overload for print that prints
    ##First Name: firstname
    ##Last  Name: lastname
class Employee (Person):
    def __init__(self, first, last, dob, ssn):
        super().__init__(first, last)
        self.dob= dob # date of birth
        self.ssn= ssn # social
    
    def get_ssn(self):
        return self.ssn # method to return ssn

    def __str__(self):
        return super().__str__() + "\nDOB: " + str(self.dob) + "\nSSN:" +str(self.get_ssn())
        



#Make derived class "Employee" that inherits the base class Person
#In the constructor, grab all the Person methods using the super() method
#(1) Add a new variable to hold date of birth called "dob" to the __init__
#   Overload __str__ with super and add "\nDOB: " + str(self.dob)
#(2) Also add a new variable "ssn" to the __init__ to hold the social security number
#    Add a new method called get_ssn that returns the ssn


if __name__=="__main__":

    ##Test situation
    """
    boss = Person("Hamed", "Haq")
    empl = Employee("Ted", "McMaster", "03151970", 999999999)

    print(boss)
    print(empl)
    print(empl.get_ssn())
    """


