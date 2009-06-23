class Hello(object):
    """
    Demonstrates a basic class and object 
    """
    def nothing(self):
        print "India is my country"
x = Hello()
x.nothing()

class Student:
    """
    A very simple class definition
    """
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def __repr__(self):
        return "%s %s %s" % (self.name, self.age, self.gender)

s = Student("ranga", 24, "m") 
print s

class add1:
    """
    Define operator for class
    """
    def __init__(self,value=0):
        self.data = value
    def __add__(self , num):
        self.data += num
class add2(add1):
    def __repr__(self):
        return 'add2(%s)' % self.data
x = add2(2)
x+1
print x
add2(3)
print str(x), repr(x)



class Prod:
    """class call"""
    def __init__(self, value):
        self.value = value
    def __call__(self, value2):
        return self.value * value2

x = Prod(2)
print x(3),x(4)

class Worker:
    """
    User-Defined Classes
    """
    def __init__(self, name, pay):            
        self.name = name                      
        self.pay  = pay
                                  
    def lastName(self):
        return self.name

    def totsal(self, percent):
        self.pay *= (1.0 + percent)          

x = Worker('Ranga', 5000)              
y = Worker('Hari', 7000)              
print x.lastName()                        
print y.lastName()                        
y.totsal(.10)                           
print y.pay


class Life:
    def __init__(self, name='unknown'):
        print 'Hello', name
        self.name = name
    def __del__(self):
        print 'Goodbye', self.name

a = Life('ranga')
a = 'hari'
print "Before delete"
print a
del a
print "after delete"
