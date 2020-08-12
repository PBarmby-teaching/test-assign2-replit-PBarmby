#for i in range(0,10):
#  print(i)
#print("all done")
#import numpy as np
#a = np.ones((5,5))
#print(a[1:3,1:3])

def myfunc(x=27, checkprime = True):
  if checkprime:
    isprime = True
    for i in range(2,x):
      if x % i == 0:
        isprime = False
        break
    return(isprime)
  else:
    return(x/3)

print(myfunc(29, checkprime=False))
