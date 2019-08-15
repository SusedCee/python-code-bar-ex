class Member():
	def __init__(self, full_name):
		self.full_name = full_name
	def hello(self):
		print(f"Hi, my name is " + self.full_name + ".")

class Student(Member):
	def __init__(self, full_name, reason):
		Member.__init__(self, full_name)
		self.reason = reason
		print("I am " + self.full_name + " - " + self.reason)

class Instructor(Member):
	def __init__(self, full_name, bio):
		Member.__init__(self, full_name)
		self.bio = bio
		self.skills = []
	def add_skill(self, skillToAdd):
		self.skills.append(skillToAdd)
		print("I am " + self.full_name + " - " + self.bio)
		print(self.skills)

class Workshop():
	def __init__(self, date, subject):
		self.date = date
		self.subject = subject
		self.instructors = []
		self.students = []

		#maybe define instructors and students as empty arrays here?

	def add_participant(self, memberToAdd):
		if isinstance(memberToAdd, Student):
			self.students.append(memberToAdd)
		else:
			self.instructors.append(memberToAdd)
	def print_details(self):
			print(f"The workshop will be on " + self.date + " and the subject is " + self.subject)

workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()
jane.hello()
lena.hello()
vicky.hello()
nicole.hello()

