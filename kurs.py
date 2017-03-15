# python kurs WDM

#help(5)

meineZahl = 3
meineZahl += 3
meineZahl -= 3

print(meineZahl)

string = 'Hallo'
string += ' Welt!'

print(string)

a = 23
b = 42
b, a = a, b

mydict = {"Key 1": "Value 1", 2: 3, "pi": 3.14}

print(mydict['pi'])
print(mydict['Key 1'])
print(mydict[2])
#print(mydict[0])

sample = [1, ["another", "list"], ("a", "tuple")]
mylist = ["List item 1", 2, 3.14]
mylist[0] = "List item 1 again" # We're changing the item.
mylist[-1] = 3.21 # Here, we refer to the last item.

import numpy as np

data = np.array([[10.3, 1.2, 1.7],
                 [2.1, 10.6, 4.6],
                 [1.2, 5.2, 8.74],
                 [5.6, 7.4, 5.45],
                 [3.8, 3.8, 2.32]])
print(data)
print(data[:,1])
print(data[1,:])

print("X: %s mm Y: %s mm Z: %s mm" % (42, 23, 0.01))

print("This %(verb)s a %(noun)s." % {"noun": "test", "verb": "is"})

#a little bit of randomness
from random import randint as zufallsInt
zufallsZahl = zufallsInt(1,5000)
print(zufallsZahl)

rangelist = range(10)
print(rangelist)
for number in rangelist:
    # Check if number is one of
    # the numbers in the tuple.
    if number in (3, 4, 7, 9):
        # "Break" terminates a for without
        # executing the "else" clause.
        break
    else:
        # "Continue" starts the next iteration
        # of the loop. It's rather useless here,
        # as it's the last statement of the loop.
        continue


if rangelist[1] == 2:
    print("The second item (lists are 0-based) is 2")
else:
    pass

#list comprehensions

erster = [1,2,3,4,5]
zweiter = [10, 100, 1000, 10000, 100000]
listComprehension = [x*y for x in erster for y in zweiter]
print(listComprehension)
len(listComprehension)

sum(1 for i in [3, 3, 4, 4, 3] if i == 4)

#bad programming
def crazyFunc(a, b, addOne=False, additor=0):
    #return some fraction of a/b+1+n
    if addOne==True:
        return a/b+1
    elif additor!=0:
        return a/b+additor
    else:
        return a/b

#better ... yet not good
def crazyFunc2(a, b, addOne=False, additor=0):
    #return some fraction of a/b+1+n
    if addOne==True:
        z = a/b+1
    elif additor!=0:
        z = a/b+additor
    else:
        z = a/b
    return z

z = crazyFunc(3,2,addOne=True,additor=1)
print(z)


def fehlerfehler():
    try:
        1 / 0
        #das universum kaputt
    except ZeroDivisionError:
        print("Nix da duch Null teilen.")
    else:
        pass
        #you may pass
    finally:
        #finally something is being done
        print("Noch was gemacht.")

fehlerfehler()

class meineKlasse(object):
    allgeminErreichbar = 10
    def __init__(self):
        self.meineVariable = 3
    def meineFunktioninMeinerKlasse(self, arg1, arg2):
        return self.meineVariable

#achtung was der scope ist!!!!


def ändertNix():
    # This will correctly change the global.
    x = 3

def ändert():
    global x
    # This will correctly change the global.
    x = 3

x = 2
ändertNix()
print(x)
ändert()
print(x)

import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])
plt.ylabel('Y LABEL')
plt.xlabel('xxx')

plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.ticker import NullFormatter  # useful for `logit` scale

# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

plt.plot(x, y - y.mean())
plt.yscale('log', linthreshy=0.01)
plt.title('log')
plt.grid(True)
plt.show()
