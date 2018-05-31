import time
import json
import pygal
from datetime import datetime, timedelta

class Session(object):
    
    def __init__(self, track):
        #Track that user's session took place at
        self.track = track
        #List of lap times user ran during session
        self.lapTimes = []
        #fastest lap user randuring session
        self.fastestLap = 999999.9
        #last lap time that the user ran this session
        self.lastLap = 0
        #total number of laps ran this session
        self.totalLaps = 0
        #total miles ran this session
        self.milesRan = 0
        #total calories burned this session
        self.caloriesBurned = 0
        #average speed of runner this session
        self.avgSpeed = 0
        #average lap time of runner this session
        self.avgLapTime = 0.0
        #time user started running this session
        self.startTime = time.time()
        #time user stopped running this session
        self.endTime = time.time()

    def print(self):
        print('Session Track: ') 
        print(self.track.name)
        print('Fastest Lap: ')
        print(self.fastestLap)
        print('Last Lap: ')
        print(self.lastLap)
        print('Total Laps Ran: ')
        print(self.totalLaps)
        print('Miles Ran: ')
        print(self.milesRan)
        print('Claories Burned: ')
        print(self.caloriesBurned)
        print('Average Speed: ')
        print(self.avgSpeed)
        print('\n')
        
class Runner(object):

    def __init__(self, weight, height, sex, name, idNum):
        """
        Requires: nothing
        Modifies: self (this instance of the Runner object)
        Effects:  This is the Runner constructor.
        """
        #user's average speed overall
        self.avgSpeed = 0.0
        #user's average laptime overall
        self.avgLapTime = 0.0
        #total number of miles ran by user
        self.milesLogged = 0.0
        #user's waeight in kilograms (expected to be entered in pounds, converted for kCal formula)
        self.weight = (weight * 0.45)
        #User's name
        self.name = name
        #User's unique identification number (possibly Google Client ID + WristbandIDNum / cvButton?
        self.idNum = idNum
        #Tracks that the user has registered with
        self.tracks = []
        #user's current running session
        self.currentSession = Session(Track('', 0))
        #list of all sessions user has ran
        self.sessions = []



        #fix this
        self.lapRecords = []

    def print(self):
        print('Runner Name: ') 
        print(self.name)
        print('Runner ID: ') 
        print(self.idNum)
        print('Miles Ran: ')
        print(self.milesLogged)
        print('Average Speed: ')
        print(self.avgSpeed)
        print('\n')

    def addLap(self, lapTime):
        """
        Requires: nothing
        Modifies: self (this instance of the Runner object)
        Effects:  
        """
        #self.lapTimes.append(lapTime)
        #if lapTime < self.lapRecord:
        #   self.lapRecord = lapTime
        self.lastLap = lapTime
        #self.totalLapsRan += 1
        self.milesLogged += self.currentSession.track.length
        
        self.currentSession.lastLap = lapTime
        self.currentSession.totalLaps += 1
        self.currentSession.lapTimes.append(lapTime)
        self.addCalories(lapTime)
        self.calculateAverageSpeed()
        self.currentSession.milesRan += self.currentSession.track.length
        if lapTime < self.currentSession.fastestLap:
            self.currentSession.fastestLap = lapTime
        
    def addCalories(self, lapTime):
        """
        Requires: nothing
        Modifies: self (this instance of the Runner object)
        Effects:  This is the Runner constructor.
        """
        smallest = 999
        smallestMETS = 9999
        with open('METS.json') as json_data:
            d = json.load(json_data)
            for i in range(len(d.keys())):
                if (self.calculateLapSpeed(self.currentSession, lapTime) / float(list(d.keys())[i])) >= 1:
                    if (self.calculateLapSpeed(self.currentSession, lapTime) / float(list(d.keys())[i])) < smallest:
                        smallestMETS = float(list(d.values())[i])
                        smallest = (self.calculateLapSpeed(self.currentSession, lapTime) + float(list(d.keys())[i])) / 2
        METS = smallestMETS
        Kcal= 0 
        self.currentSession.caloriesBurned += (METS * self.weight * (((lapTime) / 60) / 60))


    def addAvgCalories(self):
        """
        Requires: nothing
        Modifies: self (this instance of the Runner object)
        Effects:  This is the Runner constructor.
        """
        smallest = 999
        smallestMETS = 9999
        with open('METS.json') as json_data:
            d = json.load(json_data)
            for i in range(len(d.keys())):
                if (self.currentSession.avgSpeed / float(list(d.keys())[i])) >= 1:
                    if (self.currentSession.avgSpeed / float(list(d.keys())[i])) < smallest:
                        smallestMETS = float(list(d.values())[i])
                        smallest = (self.currentSession.avgSpeed + float(list(d.keys())[i])) / 2
        
        totalTime = 0
        METS = smallestMETS
        for i in range(len(self.currentSession.lapTimes)):
            totalTime += self.currentSession.lapTimes[i]
        
        self.currentSession.caloriesBurned = (METS * self.weight * (((totalTime) / 60) / 60))          
        
        
    def newSession(self, session):
        """
        Requires: nothing
        Modifies: self (this instance of the Runner object)
        Effects:  This is the Runner constructor.
        """
        self.currentSession.track.currentRunners.remove(self)
        self.currentSession.endTime = time.time()
        self.currentSession = session
        self.currentTrack = session.track
        session.track.currentRunners.append(self)
        session.track.runners.append(self)
        self.sessions.append(session)
        caloriesBurned = []
        times = []
        for i in range(len(self.sessions)):
            if self.sessions[i].caloriesBurned != 0:
                caloriesBurned.append(self.sessions[i].caloriesBurned)
                times.append(datetime.fromtimestamp(int(self.sessions[i].startTime)).strftime('%Y-%m-%d %H:%M:%S'))
                #print(self.sessions[i].caloriesBurned)



        
        
        date_chart = pygal.Line(x_label_rotation=20)
        date_chart.x_labels = map(str, times)
        date_chart.add("Calories Burned", caloriesBurned)
        date_chart.render_to_file('calories'+ str(self.idNum) + '.svg')  
        
    def setCurrentTrack(self, track):
        """
        Requires: nothing
        Modifies: self (this instance of the Runner object)
        Effects:  This is the Runner constructor.
        """
        self.currentTrack = track
       # if self not in track.currentRunners:
           # track.addCurrentRunner(self)
    def calculateLapSpeed(self, session, laptime):
        """
        Requires: nothing
        Modifies: self (this instance of the Runner object)
        Effects:  This is the Runner constructor.
        """
        return session.track.length / (laptime / 3600)

    def calculateAverageSpeed(self):
        """
        Requires: nothing
        Modifies: self (this instance of the Runner object)
        Effects:  This is the Runner constructor.
        """
        average = 0
        iterator = 0
        if len(self.sessions) >= 1:
            for i in range(len(self.sessions)):                
                for j in range(len(self.sessions[i].lapTimes)):
                    iterator += 1
                    average += self.calculateLapSpeed(self.sessions[i], self.sessions[i].lapTimes[j])
                    
        average = average / iterator
        self.avgSpeed = average
        average = 0
        for i in range(len(self.currentSession.lapTimes)):
            average += self.calculateLapSpeed(self.currentSession, self.currentSession.lapTimes[i])
        average = average / len(self.currentSession.lapTimes)
        self.currentSession.avgSpeed = average
        
class Track(object):

    def __init__(self, name, length):
        
        self.length = length #Miles
        self.name = name
        self.runners = []
        self.currentRunners = []
    def addRunner(self, runner):
        self.runners.append(runner)
    def addNewRunner(self, weight, height, sex, name, idNum):
        self.runners.append(Runner(weight, height, sex, name, idNum))

    def addCurrentRunner(self, runner):
        runner.setCurrentTrack(self)
        runner.currentSession.track = self
        runner.sessions.append(runner.currentSession)
        self.currentRunners.append(runner)
        
    def removeCurrentRunner(runner):
        self.currentRunners.remove(runner)

    def print(self):
        print('name: ')
        print(self.name)
        print('length (miles): ')
        print(self.length)
        print('runners: ')
        for i in range(len(self.currentRunners)):
            print(self.currentRunners[i].name)
        print('current runners: ')
        for i in range(len(self.runners)):
            print(self.runners[i].idNum)
        print('\n')
            
        
class tracker(object):
    def __init__(self):
        self.tracks = []
        self.runners = []
    def addTrack(self, name, length):
        self.tracks.append(Track(name, length))

    def addRunner(self, runner):
        self.runners.append(runner)

    def print(self):
        for i in range(len(self.tracks)):
            self.tracks[i].print()
        for i in range(len(self.runners)):
            self.runners[i].print()
            
    
    
