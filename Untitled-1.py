
class students:
    def __init__(self):
        self.student= []

    def mark_present(self,s):
        if s not in self.student:
            self.student.append(s)
            print("add successful")

        else:
            print("not added")

    def remove_student(self,s):
        if s in self.student:
            self.student.remove(s)
            print("removed")

        else:
            print("not removed as not present")

    def is_present(self,s)->bool:
        if s in self.student:
            print("the entered student is present ")
            return True
        else:
            print("the enetered student is nor present")
            return False
        
    def display_attendence(self):
        if self.student:
            for i in self.student:
                print(i)

        else:
            print("empty list")

s=students()
s.mark_present("karan")
s.mark_present("rahul")
s.mark_present("james")
s.mark_present("frank")
s.mark_present("oppoi")
s.display_attendence()

s.remove_student("karan")
s.display_attendence()

s.is_present("rahul")





        
