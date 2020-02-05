
class SchoolSubjects:
    def __init__(self, period, duration_of_period):
        self.period = period
        self.duration_of_period = duration_of_period

    def classes(self):
        print("It is currently " + self.period + ".")
        print(self.duration_of_period)


p1 = SchoolSubjects("first period", "8:47-9:47")
p2 = SchoolSubjects("second period ", "9:49-10:34")
recess = SchoolSubjects("recess", "10:38-11:05")
p3 = SchoolSubjects("third period", "11:08-11:50")
p4 = SchoolSubjects("fourth period", "11:53-12:38")
p5 = SchoolSubjects("fifth period", "12:41-13:26")
p6 = SchoolSubjects("sixth period", "13:28-14:13")
p7 = SchoolSubjects("seventh period", "14:15-15:00")
