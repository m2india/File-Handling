import datetime
import re

class Address:



	def __init__(self):

		self.name = input("What is your Name : ")

		self.email = input("What is your Email id: ")

		#Email Id Validations

		regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
		EmailAddsVerify = str(self.email)
		match = re.match(regex, EmailAddsVerify)

		if match == None:
			print('Bad Syntax')
			raise ValueError('Bad Syntax')


	def fileOpen(self):

		try:
			f = open("Register_Details.txt",'a', encoding = 'utf-8')

			now = datetime.datetime.now()

			#name = input("Enter your name?")

			f.write("Name : %s  Email : %s Time : %s \r\n" % (self.name, self.email, now.strftime("%Y-%m-%d %H:%M")))

		except:
			print("Something went wrong")	
		else:
			print("Successfull Register Details ")		
		finally:
   			f.close()	

c = Address()
c.fileOpen()
	