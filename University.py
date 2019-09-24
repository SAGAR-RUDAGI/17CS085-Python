class Student:
	def __init__(self):
		self.id = None
		self.age = None
		self.marks = None

	def validate_marks(self):
		return self.marks >= 0 and self.marks <=100

	def validate_age(self):
		return self.age>20

	def check_qualifications(self):
		if(self.validate_marks() and self.validate_age()):
			return self.marks>=65
		else:
			return False

	def set(self):
		self.id = input("ID {example:1BM17CS000} : ")
		self.age = int(input("AGE : "))
		self.marks = float(input("Marks : "))

	def get(self):
		print("ID : ",self.id)
		print("AGE : ",self.age)
		print("MARKS : ",self.marks)

S = Student()
S.set()
S.get()
print(S.check_qualifications())