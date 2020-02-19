# moon phase calculator
# will give an indication of the currnet size of the moon (UK time)

from datetime import datetime
from datetime import timedelta
from decimal import Decimal

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
    phase = Decimal(p1)                 # percentage of current cycle 0% & 100% being new 50% being full
    daynum = 29.53 * float(phase)

    #determining lunar phase name 
    if 0 <= phase < 0.11:
        print ("Lunar Phase: New, day {:.1f}" .format(daynum))
        return phase
    elif 0.11 <= phase < 0.22:
        print("Lunar Phase: Waxing Cresent, day {:.1f}" .format(daynum))
        return phase
    elif 0.22 <= phase < 0.33:
        print("Lunar Phase: First Quarter, day {:.1f}" .format(daynum))
        return phase
    elif 0.33 <= phase < 0.44:
        print("Lunar Phase: Waxing Gibbous, day {:.1f}" .format(daynum))
        return phase
    elif 0.44 <= phase < 0.55:
        print("Lunar Phase: Full, day {:.1f}" .format(daynum))
        return phase
    elif 0.55 <= phase < 0.66:
        print("Lunar Phase: Waning Gibbous, day {:.1f}" .format(daynum))
        return phase
    elif 0.77 <= phase < 0.88:
        print("Lunar Phase: Third Quarter, day {:.1f}" .format(daynum))
        return phase
    elif 0.88 <= phase < 1:
        print("Lunar Phase: Waning Crescent, day {:.1f}" .format(daynum))
        return phase
    else:
        print("error")
        pass

#determining moon size as percentage
def moon_size (phase):
    if phase <= 0.5:
        size = 200*phase
        print("Moon Size: {0:.2f}%".format(size))
        return size
    elif 0.5 < phase < 1:
        size = 200*(1-phase)
        print("Moon Size: {0:.2f}%".format(size))
        return size
    else:
        print("error")
        pass

# main path of program
lunar_phase();
moon_size(phase);



