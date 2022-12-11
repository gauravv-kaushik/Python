class student:
 def __init__(self):
   self.name=input("enter your name ")
   self.n1=int(input("enter your marks in maths "))
   self.n2=int(input("enter your marks in physics "))
   self.n3=int(input("enter your marks in chemistry "))
 def avg(self):
   return ((self.n1+self.n2+self.n3)/3)
 def display(self):
   print("Name = ",self.name)
   print("Marks of first subject i.e Maths is = ",self.n1)
   print("Marks of second subject i.e Physics is = ",self.n2)
   print("Marks of third subject i.e Chemisty is = ",self.n3)
   print("Average Marks are = ",self.avg())
marks = student( )
marks.display( )
