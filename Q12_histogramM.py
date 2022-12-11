# Q12. Write a program that makes use of a function to accept a list of n  integers and displays a histogram.

#plotting histogram
import matplotlib.pyplot as plt   #importing the module

def plothistogram(data):
  plt.hist(data)                   #plot histogram ;  By default it take maximum 10 no. of bins
  plt.xlabel('VALUES')             #y default xdustance of each bin is about 0.5 units
  plt.ylabel('FREQUENCY')
  plt.title('HISTOGRAM')
  plt.xlim(min(data)-1 , max (data)+1)    #defining limits 
  plt.show()                        

def main():
  data = eval(input('Enter data to be plotted as histogram'))
  plothistogram(data)

if __name__ == "__main__" :
  main()
