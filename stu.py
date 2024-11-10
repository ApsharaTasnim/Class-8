class student:
    grade=11
    name="Apshara."
    def introduction(self):
        print("Hello!I am a student.")
    def details(self):
        print("I am in grade ",self.grade)
        print("My name is ",self.name)
ob=student()
ob.introduction()
ob.details()