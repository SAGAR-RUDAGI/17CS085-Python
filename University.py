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

S = Student()
S.set()
S.get()
print(S.check_qualifications())
