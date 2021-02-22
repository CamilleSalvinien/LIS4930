#1
from datetime import datetime
time = datetime.now()
print(time.strftime("%H:%M:%S"))

#2
from datetime import timedelta
time = datetime.now()

timeInFuture = time - timedelta(seconds=60) + timedelta(days=730)
print(timeInFuture)

#3
from datetime import timedelta
timeObject = timedelta(days=100,hours=10,minutes=13)
print(timeObject)


#4
feet, inches = map(int,input("Please input your height: ").split())
inches += feet*12
centimeter = round(inches*2.54,3)

print(centimeter)

############################

#itertools




#infinite iterators



#itertools cycle




#iterrools repeat

