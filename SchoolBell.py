import datetime
import pyaudio
import wave
import sys
import time

script, filemame = sys.argv

datetime_object = datetime.datetime.now()

wf = wave.open(sys.argv[1], 'rb')

CHUNK = 1024

p = pyaudio.PyAudio()
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

audio = wf.readframes(CHUNK)

time1 = datetime.time(14,5,0)
time2 = datetime.time(13,54,0)
time3 = datetime.time(8,47,0)
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


print(timeNow)


while True:
    for x in listOfTimes:
        if (x == timeNow):
            print("Success!")
#            stream.write(audio)
#            audio = wf.readframes(CHUNK)





class TimeStrings:
    def __init__(self, period, startTime, endTime):
        self.period = period
        self.startTime = startTime
        self.endTime = endTime

    def screenOutput(self):
        print('It is currently ' + self.period + '.')
        print(self.startTime, self.endTime)

tp1 = TimeStrings('devotions', '8:15 -', '8:45')
tp2 = TimeStrings('first period', '8:47 -', '9:46')
tp3 = TimeStrings('second period', '9:49 -', '10:34')
tp4 = TimeStrings('recess', '10:38 -', '11:05')
tp5 = TimeStrings('third period', '11:08 -', '11:50')
tp6 = TimeStrings('fourth period', '11:53 -', '12:38')
tp7 = TimeStrings('fifth period', '12:41 -', '13:26')
tp8 = TimeStrings('sixth period', '13:28 -', '14:13')
tp9 = TimeStrings('seventh period', '14:15 -', '15:00')
