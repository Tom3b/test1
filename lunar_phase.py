# moon phase calculator
# will give an indication of the currnet size of the moon (UK time)

from datetime import datetime
from datetime import timedelta
import math

#determining lunar phase
def lunar_phase ():
    # calculating days since known new moon date
    d1 = datetime.now()
    d2 = datetime(2020, 1, 24, 21, 42)
    delta = d1 - d2
    days = delta.days
    seconds = delta.seconds / 86400     # 86400 seconds in a day
    timesn = days + seconds             # time since new moon
    p1 = timesn / 29.53                 # new moon repeats every 29.53 days
    global phase
    phase1 = math.floor(p1)             # removal of extra months 
    phase = (p1 / phase1) - 1
    daynum = 29.53 * float(phase)

    #determining lunar phase name        
    if 0 <= phase < 0.05 or 0.95 <= phase < 1:
        print ("Lunar Phase: New, day {:.1f}" .format(daynum))
        return phase
    elif 0.05 <= phase < 0.225:
        print("Lunar Phase: Waxing Cresent, day {:.1f}" .format(daynum))
        return phase
    elif 0.225 <= phase < 0.275:
        print("Lunar Phase: First Quarter, day {:.1f}" .format(daynum))
        return phase
    elif 0.275 <= phase < 0.475:
        print("Lunar Phase: Waxing Gibbous, day {:.1f}" .format(daynum))
        return phase
    elif 0.475 <= phase < 0.525:
        print("Lunar Phase: Full, day {:.1f}" .format(daynum))
        return phase
    elif 0.525 <= phase < 0.725:
        print("Lunar Phase: Waning Gibbous, day {:.1f}" .format(daynum))
        return phase
    elif 0.725 <= phase < 0.775:
        print("Lunar Phase: Third Quarter, day {:.1f}" .format(daynum))
        return phase
    elif 0.775 <= phase < 0.95:
        print("Lunar Phase: Waning Crescent, day {:.1f}" .format(daynum))
        return phase
    else:
        print("error")
        pass

#determining moon size as percentage
def moon_size (phase):
    # moon size is non linear to day in calendar
    if phase <= 0.5:
        size = 100 * (0.5 + 0.5 * math.sin((float (phase) * 2 * 3.14159) - 1.57096))
        print("Moon Size: {0:.2f}%".format(size))
        return size
    elif 0.5 < phase < 1:
        size = 100 * (0.5 + 0.5 * math.sin(((1 - float(phase)) * 2 * 3.14159) - 1.57096))
        print("Moon Size: {0:.2f}%".format(size))
        return size
    else:
        print("error")
        pass

# main path of program
lunar_phase();
moon_size(phase);
