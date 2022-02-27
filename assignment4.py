#QUESTION 1
print("ANSWER 1")
def TowerOfHanoi(n , fromRod, toRod, auxRod):
	if n == 0:
		return
	TowerOfHanoi(n-1, fromRod, auxRod, toRod)
	print("Move disk",n,"from rod",fromRod,"to rod",toRod)
	TowerOfHanoi(n-1, auxRod, toRod, fromRod)
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')
print("\n")

#QUESTION 2
print("ANSWER 2")
from math import factorial

n=int(input('Enter the size of pascals triangle '))

print("USING LOOPS")

for i in range(n):
	for j in range(n-i+1):
		print(end=" ") #for spacing

	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")	# nCr = n!/((n-r)!*r!)
	print()	# for new line
print("\n\n")

print("USING RECURSSIONS")

def pascal_triangle(n,originalength=n):
    if n == 0:
        return
    pascal_triangle(n-1,originalength)
    #printing the spaces
    print('  '*(originalength-n), end='  ')

    #starting from 1
    start = 1
    for i in range(1, n+1):

        print(start, end ='   ')
        
        #using Binomial Coefficient
        start = start * (n - i) // i
    print()
pascal_triangle(n)
print("\n")



#Question 3
print("Question 3")
num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number(not zero): "))
quotient=num1//num2
remainder=num1%num2

def check0(input):
    if input ==0:
        print()

#part a
print("Part A")

print("Checking if callable or not!")
print("Quotient:",callable(quotient))
print("Remainder:",callable(remainder))
print()
#part b

print("Part B:")
if (num1 and num2 and quotient and remainder)!=0:
    print("All values are non zero!!")

elif num1 == 0 or num2 == 0 or quotient == 0 or remainder == 0:
    print("Not all values are non zero")
print()
#part c        
print("Part C")

displaylist=[num1,num2,quotient,remainder]
displaylist= displaylist+[4,5,6]
for i in displaylist:
    if i>4:
        print(i)

print("Done")        
print()
#part D
print("Part D")
setdata=set(displaylist)
print("Done")
print("Set is",setdata)
print()
#part E
print("Part E")
immutableset=frozenset(setdata)
print("Done")
print(immutableset)
print()
#Part F
print("Part F")
print("Hash value of maximum of set:",(hash(max(immutableset))))

#Question 4
print("Question 4")
class Student():
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        print("Object created!")

    def __del__(self):
        print(" Object deleted")


s1=Student("Chaitanya",20)
print("Object created with name:",s1.name,"and roll no:",s1.rollno)
del s1


#QUESTION 5
print("ANSWER 5")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
#creating employee records
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

#part a updating salary
employee1.salary = 70000
print("The updated salary of",employee1.name ,"is",employee1.salary)
#part b deleting a record
print("<b>Record of Viren deleted")
del employee3
print("\n")

#question 6
print("Question 6")
remake=""
word=""
def wordentry():
    global word
    word=input("George enter a word:")
    
def remakeword():
    global remake
    remake=input("Barbie rearange the word and enter:")
    verify()


      

def verify():
    if len(word) == len(remake):
        entrylist=list(word)
        remakelist=list(remake)
        for i in entrylist:
            if i in remakelist:
                continue
            else:
                print("Freindship is fake!")
                break

        shopverification()    

    else:
        print("Wrong word!!")
        print("Friendship is fake!")
        print("Try again")
        remakeword()

def shopverification():
    print()
    validinput=input("Is above word is valid(Y or N)??")
    if validinput.lower()=="y":
        print("True friendhip")
    elif validinput.lower()=="n" :
        print("Fake friendship")   

    else:
        print("invalid input taking to option again")
        shopverification()


wordentry()
remakeword()
