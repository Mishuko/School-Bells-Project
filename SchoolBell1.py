import datetime
from tkinter import *
from playsound import playsound
import sys
import time

datetime_object = datetime.datetime.now()

time1 = datetime.time(7,45,0)
time2 = datetime.time(8,12,0)
time3 = datetime.time(8,15,0)
time4 = datetime.time(8,45,0)
time5 = datetime.time(8,47,0)
time6 = datetime.time(9,32,0) #45 minute bell
time7 = datetime.time(9,47,0)
time8 = datetime.time(9,49,0)
time9 = datetime.time(10,34,0)
time10 = datetime.time(10,39,0)
time11 = datetime.time(11,5,0)
time12 = datetime.time(11,8,0)
time13 = datetime.time(11,50,0)
time14 = datetime.time(11,53,0) #kids' lunch starts
time15 = datetime.time(12,17,0) #kids' fove-minute warning
time16 = datetime.time(12,23,0) #kids' lunch ends
time17 = datetime.time(12,38,0) #end of fourth period
time18 = datetime.time(12,41,0) #start of fifth period
time19 = datetime.time(12,56,0) #lunch bell
time20 = datetime.time(13,21,0) #five-minute warning
time21 = datetime.time(13,26,0) #end of fifth period
time22 = datetime.time(13,28,0) #start of sixth period
time23 = datetime.time(14,13,0) #end of sixth period
time24 = datetime.time(14,15,0) #start of seventh period
time25 = datetime.time(15,0,0)  #end of seventh period
timeNow = datetime.time(datetime_object.hour, datetime_object.minute,datetime_object.second)

StartOfPeriod = [time1, time3, time5, time6, time8, time10,
time12, time14, time17, time21, time23]

EndOfPeriod = [time2, time4, time7, time9, time11,
time13, time16, time20, time22, time24]

LunchBell = [time14, time19]

LunchWarning = [time15, time20]

class TimeStrings:
    def __init__(self, period, startTime, blankSpace, endTime):
        self.period = period
        self.startTime = startTime
        self.blankSpace = blankSpace
        self.endTime = endTime

    def __str__(self):
        return(str(self.period) + '. \n' + str(self.startTime) + self.blankSpace + str(self.endTime))


tp1 = TimeStrings('School door should be open.', str(time1), ' - ', time2)
tp2 = TimeStrings('Devotions start in 3 minutes.', str(time2), ' - ', time3)
tp3 = TimeStrings('We are in devotions.', str(time3), ' - ', time4)
tp4 = TimeStrings('The first period starts in 2 minutes.', str(time4), ' - ', time5)
tp5 = TimeStrings('We are in first period.', str(time5), ' - ', time7)
tp6 = TimeStrings('Second period starts in 2 minutes.', str(time7), ' - ', time8)
tp7 = TimeStrings('We are in second period.', str(time8), ' - ', time9)
tp8 = TimeStrings('Be ready for recess in 5 minutes.', str(time9), ' - ', time10)
tp9 = TimeStrings('Third period starts in 3 minutes.', str(time11), ' - ', time12)
tp10 = TimeStrings('It is currently recess.', str(time10), ' - ', time11)
tp11 = TimeStrings('It is third period.', str(time12), ' - ', time13)
tp12 = TimeStrings('We are in fourth period period. Lower scool is from 11:53 - 12:23', str(time14), ' - ', time17)
tp13 = TimeStrings('Fifth period starts in 2 minutes.', str(time17), ' - ', time18)
tp14 = TimeStrings('We are in fifth period. Upper school lunch is from 12:56 - 1:26', str(time18), ' - ', time20)
tp15 = TimeStrings('Sixth period starts in  2 minutes.', str(time20), ' - ', time21)
tp16 = TimeStrings('We are in sixth period.', str(time21), ' - ', time22)
tp17 = TimeStrings('Seventh period starts in 2 minutes.', str(time22), ' - ', time23)
tp18 = TimeStrings('We are in seventh period', str(time23), ' - ', time24)
tp19 = TimeStrings('The school day is over!', ' ', ' ', ' ')


while True:
    datetime_object = datetime.datetime.now()
    timeNow = datetime.time(datetime_object.hour, datetime_object.minute, datetime_object.second)

    for x in StartOfPeriod:
        if (x == timeNow):
            playsound('start.wav')

    for x in EndOfPeriod:
        if (x == timeNow):
            playsound('end.wav')

    for x in LunchBell:
        if (x == timeNow):
            playsound('lunchwarning.wav')

    for x in LunchWarning:
        if (x == timeNow):
            playsound('five.mp3')


    if (time1 == timeNow):
        print(tp1)
    if (time2 == timeNow):
        print(tp2)
    if (time3 == timeNow): #start of devotions
        print(tp2)
    if (time4 == timeNow): #end
        print(tp4)
    if (time5 == timeNow): #start
        print(tp5)
    if (time7 == timeNow): #end
        print(tp6)
    if (time8 == timeNow): #start
        print(tp7)
    if (time9 == timeNow):
        print(tp8)
    if (time10 == timeNow):
        print(tp9)
    if (time11 == timeNow):
        print(tp10)
    if (time12 == timeNow):
        print(tp11)
    if (time13 == timeNow):
        print(tp12)
    if (time14 == timeNow):
        print(tp13)
    if (time15 == timeNow):
        print(tp14)
    if (time17 == timeNow):
        print(tp15)
    if (time18 == timeNow):
        print(tp16)
    if (time19 == timeNow):
        print(tp17)
    if (time20 == timeNow):
        print(tp18)
    if (time21 == timeNow):
        print(tp19)
