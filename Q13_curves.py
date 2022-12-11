# Q13.Write a program that makes use of a function to display sine,cosine,polynomial and exponential curves. 


# ***** SINE CURVES *****
# plotting sinecurve
import math
import matplotlib.pyplot as plt
def sineCurve():
  plt.subplot(2,1,1)
  degrees=range(0,360+1)
  sineValues = [math.sin(math.radians(i)) for i in degrees]
  plt.plot(sineValues)
  plt.xlabel('Degree')
  plt.ylabel('Sine Values')
  plt.title('Sine Curve')
  plt.grid()
def main():
  sineCurve()
  plt.tight_layout()
  plt.show()
if __name__=="__main__":
  main() 



# ***** COSINE CURVES *****
 # plotting cosinecurve
import math
import matplotlib.pyplot as plt
def cosineCurve():
  plt.subplot(2,1,2)
  degrees=range(0,360+1)
  cosineValues = [math.cos(math.radians(i)) for i in degrees]
  plt.plot(cosineValues)
  plt.xlabel('Degree')
  plt.ylabel('Sine Values')
  plt.title('Cosine Curve')
  plt.grid()
def main():
  cosineCurve()
  plt.tight_layout()
  plt.show()
if __name__=="__main__":
 main() 



# ***** EXPONENTIAL CURVES *****
 # plotting exponentialcurve
import math
import matplotlib.pyplot as plt
def ExponentialCurve():
  val=range(0,5+1)
  exponent=[math.exp(i) for i in val]
  plt.plot(exponent)
  plt.xlabel('x values')
  plt.ylabel('y Values')
  plt.title('Exponential Curve')
  plt.grid()
def main():
  ExponentialCurve()
  plt.show()
if __name__=="__main__":
  main() 



# ********** POLYNOMIAL CURVE **********
def PolynomialCurve():
  plt.subplot(2,1,2)
  y=[]
  plt.xlim(0,100)
  sum = 0
  for x in range(0,100):
    y.append(3*x**2 + 2*x + 1)
  plt.plot(y,'m',linewidth = 2.2)
  plt.xlabel('VALUE OF N')
  plt.ylabel('POLYNOMIAL VALUE')
  plt.title('POLYNOMIAL CURVE')
  plt.grid()
def main():
  PolynomialCurve()
  plt.show()
if __name__=="__main__":
  main() 
