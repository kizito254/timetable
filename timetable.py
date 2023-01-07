class University:
    def __init__(self, name):
        self.name = name
        self.courses = []
    
    def add_course(self, course):
        self.courses.append(course)
    
    def get_timetable(self):
        timetable = {}
        for course in self.courses:
            for time, location in course.timetable.items():
                timetable[time] = location
        return timetable

class Course:
    def __init__(self, name, timetable):
        self.name = name
        self.timetable = timetable

# Create a new university
university = University("Example University")

# Create some courses with timetables
course1 = Course("Computer Science 101", {
    "Monday 10:00": "Room 101",
    "Wednesday 14:00": "Room 102"
})

course2 = Course("English Literature 201", {
    "Tuesday 09:00": "Room 201",
    "Thursday 11:00": "Room 202"
})

# Add the courses to the university
university.add_course(course1)
university.add_course(course2)

# Get the timetable for the university
timetable = university.get_timetable()

# Print the timetable
for time, location in timetable.items():
    print(f"{time}: {location}")
