# moon phase calculator
# will give an indication of the currnet size of the moon (UK time)

from datetime import datetime
from datetime import timedelta
from decimal import Decimal

# calculating days since known new moon date
d1 = datetime.now()
d2 = datetime(2020, 1, 24, 21, 42)
delta = d1 - d2
days = delta.days

#determining lunor phase 
seconds = delta.seconds / 86400     # 86400 seconds in a day
timesn = days + seconds             # time since new moon
p1 = timesn / 29.53                 # new moon repeats every 29.53 days
phase = Decimal(p1)                 # percentage of current cycle 0% & 100% being new 50% being full

#determining lunar phase name 
if 0 <= phase < 0.11:
    print ("Lunar phase: New")
elif 0.11 <= phase < 0.22:
    print("Lunar phase: Waxing Cresent")
elif 0.22 <= phase < 0.33:
    print("Lunar phase: First Quarter")
elif 0.33 <= phase < 0.44:
    print("Lunar phase: Waxing Gibbous")
elif 0.44 <= phase < 0.55:
    print("Lunar phase: Full") 
elif 0.55 <= phase < 0.66:
    print("Lunar phase: Waning Gibbous")
elif 0.77 <= phase < 0.88:
    print("Lunar phase: Third Quarter")
elif 0.88 <= phase < 1:
    print("Lunar phase: Waning Crescent")
else:
    print("error")

#determining moon size as percentage 
if phase <= 0.5:
    size = 200*phase
    print("Moon size: {0:.2f}%".format(size))  
elif 0.5 < phase < 1:
    size = 200*(1-phase)
    print("Moon size: {0:.2f}%".format(size))
else:
    print("error")

if 0 <= phase < 0.11:
    print ("Lunar phase: New")
elif 0.11 <= phase < 0.22:
    print("Lunar phase: Waxing Cresent")
elif 0.22 <= phase < 0.33:
    print("Lunar phase: First Quarter") 
