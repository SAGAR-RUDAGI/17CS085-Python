class Student:
	def __init__(self):
		self.__id = None
		self.__age = None
		self.__marks = None

	def validate_marks(self):
		return self.__marks >= 0 and self.__marks <=100

	def validate_age(self):
		return self.__age>20

	def check_qualifications(self):
		if(self.validate_marks() and self.validate_age()):
			return self.__marks>=65
		else:
			return False

	def set(self):
		self.__id = input("ID {example:1BM17CS000} : ")
		self.__age = int(input("AGE : "))
		self.__marks = float(input("Marks : "))

	def get(self):
		print("ID : ",self.__id)
		print("AGE : ",self.__age)
		print("MARKS : ",self.__marks)

n = int(input("No of students : "))
studs = []
for i in range(n):
	studs.append(Student())
for i in range(n):
	studs[i].set()
	studs[i].get()
	print(["Not qualified","Qualified"][studs[i].check_qualifications()])
	print()
	print()

