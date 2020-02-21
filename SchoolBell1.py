import datetime
from tkinter import *
from playsound import playsound
import sys
import time

datetime_object = datetime.datetime.now()

time1 = datetime.time(10,14,10)
time2 = datetime.time(13,38,20)
time3 = datetime.time(13,48,30)
time4 = datetime.time(9,46,0)
time5 = datetime.time(9,49,0)
time6 = datetime.time(10,34,0)
time7 = datetime.time(10,38,0)
time8 = datetime.time(11,5,0)
time9 = datetime.time(11,8,0)
time10 = datetime.time(11,50,0)
time11 = datetime.time(11,53,0)
time12 = datetime.time(12,38,0)
time13 = datetime.time(12,41,0)
time14 = datetime.time(13,26,0)
time15 = datetime.time(13,28,0)
time16 = datetime.time(14,13,0)
time17 = datetime.time(15,15,0)
time18 = datetime.time(13,36,0)
timeNow = datetime.time(datetime_object.hour, datetime_object.minute,datetime_object.second)

listOfTimes = [time1, time2, time3, time4, time5, time6, time7, time8, time9, time10,
time11, time12, time13, time14, time15, time16, time17, time18]

class TimeStrings:
    def __init__(self, period, startTime, blankSpace, endTime):
        self.period = period
        self.startTime = startTime
        self.blankSpace = blankSpace
        self.endTime = endTime

    def __str__(self):
        return('It is currently ' + str(self.period) + '. \n' + str(self.startTime) + self.blankSpace + str(self.endTime))


tp1 = TimeStrings('devotions', str(time1), ' - ', time2)
tp2 = TimeStrings('first period', str(time3), ' - ', time4)
tp3 = TimeStrings('second period', str(time5), ' - ', time6)
tp4 = TimeStrings('recess', str(time7), ' - ', time8)
tp5 = TimeStrings('third period', str(time9), ' - ', time10)
tp6 = TimeStrings('fourth period', str(time11), ' - ', time12)
tp7 = TimeStrings('fifth period', str(time13), ' - ', time14)
tp8 = TimeStrings('sixth period', str(time15), ' - ', time16)
tp9 = TimeStrings('seventh period', str(time17), ' - ', time18)


while True:
    datetime_object = datetime.datetime.now()
    timeNow = datetime.time(datetime_object.hour, datetime_object.minute, datetime_object.second)

    for x in listOfTimes:
        if (x == timeNow):
            playsound('schoolbell.wav')

    if (time1 == timeNow):
        print(tp1)
    if (time2 == timeNow):
        print(tp2)
    if (time3 == timeNow):
        print(tp3)
    if (time4 == timeNow):
        print(tp4)
    if (time5 == timeNow):
        print(tp5)
    if (time6 == timeNow):
        print(tp6)
    if (time7 == timeNow):
        print(tp7)
    if (time8 == timeNow):
        print(tp8)
    if (time9 == timeNow):
        print(tp9)
    if (time10 == timeNow):
        print(tp10)
    if (time11 == timeNow):
        print(tp11)
    if (time12 == timeNow):
        print(tp12)
    if (time13 == timeNow):
        print(tp13)
    if (time14 == timeNow):
        print(tp14)
    if (time15 == timeNow):
        print(tp15)
    if (time16 == timeNow):
        print(tp16)
    if (time17 == timeNow):
        print(tp17)
    if (time18 == timeNow):
        print(tp18)