from track import *
'''
class tracker(object):
    def __init__(self):
        tracks = []
        runners = []
    def addTrack(name, length):
        tracks.append(Track(name, length))

    def addRunner(self, runner):
        self.runners.append(runner)
'''

def main():
    
    myTrack = Track('CAC', (1/8))

    myTrack.addRunner(120, 5, 'm', 'Stan', '000')
    myTrack.addCurrentRunner(myTrack.runners[0])

    myTrack.addRunner(150, 5, 'f', 'Jane', '001')
    myTrack.addCurrentRunner(myTrack.runners[1])
    myTrack.addRunner(135, 6, 'm', 'John', '002')
    myTrack.addCurrentRunner(myTrack.runners[2])
    myTrack.addRunner(125, 6, 'm', 'Dan', '003')
    myTrack.addCurrentRunner(myTrack.runners[3])
    myTrack.addRunner(140, 5, 'f', 'Jill', '004')
    myTrack.addCurrentRunner(myTrack.runners[4])
    myTrack.addRunner(145, 6, 'm', 'Steve', '005')
    myTrack.addCurrentRunner(myTrack.runners[5])

    myTrack.currentRunners[0].addLap(60)
    myTrack.currentRunners[0].addLap(60)
    myTrack.currentRunners[0].addLap(60)
    myTrack.currentRunners[0].addLap(60)
    myTrack.currentRunners[1].addLap(60)
    myTrack.currentRunners[1].addLap(65)
    myTrack.currentRunners[1].addLap(70)
    myTrack.currentRunners[1].addLap(95)
    myTrack.currentRunners[2].addLap(90)
    myTrack.currentRunners[2].addLap(95)
    myTrack.currentRunners[2].addLap(80)
    myTrack.currentRunners[2].addLap(75)
    myTrack.currentRunners[3].addLap(60)
    myTrack.currentRunners[3].addLap(25)
    myTrack.currentRunners[3].addLap(30)
    myTrack.currentRunners[3].addLap(85)
    myTrack.currentRunners[4].addLap(60)
    myTrack.currentRunners[4].addLap(95)
    myTrack.currentRunners[4].addLap(80)
    myTrack.currentRunners[4].addLap(35)
    myTrack.currentRunners[5].addLap(40)
    myTrack.currentRunners[5].addLap(55)
    myTrack.currentRunners[5].addLap(60)
    myTrack.currentRunners[5].addLap(35)

    for i in range(len(myTrack.currentRunners)):
        #myTrack.currentRunners[i].print()
        myTrack.currentRunners[i].currentSession.print()

    

    secondTrack = Track('Fennville Field Track', (1/4))
    
    myTrack.currentRunners[0].newSession(Session(secondTrack))
    #secondTrack.runners[0].sessions[0].print()

    myTrack.currentRunners[0].newSession(Session(secondTrack))
    myTrack.currentRunners[0].newSession(Session(secondTrack))
    myTrack.currentRunners[0].newSession(Session(secondTrack))
    myTrack.currentRunners[0].newSession(Session(secondTrack))
    myTrack.currentRunners[0].newSession(Session(secondTrack))
    
    #secondTrack.print()

    secondTrack.currentRunners[0].addLap(120)
    secondTrack.currentRunners[0].addLap(120)
    secondTrack.currentRunners[0].addLap(120)
    secondTrack.currentRunners[0].addLap(120)
    secondTrack.currentRunners[1].addLap(60)
    secondTrack.currentRunners[1].addLap(65)
    secondTrack.currentRunners[1].addLap(70)
    secondTrack.currentRunners[1].addLap(95)
    secondTrack.currentRunners[2].addLap(90)
    secondTrack.currentRunners[2].addLap(95)
    secondTrack.currentRunners[2].addLap(80)
    secondTrack.currentRunners[2].addLap(75)
    secondTrack.currentRunners[3].addLap(85)
    secondTrack.currentRunners[3].addLap(85)
    secondTrack.currentRunners[3].addLap(85)
    secondTrack.currentRunners[3].addLap(85)
    secondTrack.currentRunners[4].addLap(60)
    secondTrack.currentRunners[4].addLap(95)
    secondTrack.currentRunners[4].addLap(80)
    secondTrack.currentRunners[4].addLap(35)
    secondTrack.currentRunners[5].addLap(40)
    secondTrack.currentRunners[5].addLap(55)
    secondTrack.currentRunners[5].addLap(60)
    secondTrack.currentRunners[5].addLap(35)

    for i in range(len(secondTrack.currentRunners)):
        #myTrack.currentRunners[i].print()
        secondTrack.currentRunners[i].currentSession.print()



    thirdTrack = Track('Allegan Field Track', (1/5))

        
    secondTrack.runners[0].newSession(Session(thirdTrack))
    secondTrack.runners[1].newSession(Session(thirdTrack))
    secondTrack.runners[2].newSession(Session(thirdTrack))
    secondTrack.runners[3].newSession(Session(thirdTrack))
    secondTrack.runners[4].newSession(Session(thirdTrack))
    secondTrack.runners[5].newSession(Session(thirdTrack))
    
    thirdTrack.currentRunners[0].addLap(120)
    thirdTrack.currentRunners[0].addLap(120)
    thirdTrack.currentRunners[0].addLap(120)
    thirdTrack.currentRunners[0].addLap(120)
    thirdTrack.currentRunners[1].addLap(60)
    thirdTrack.currentRunners[1].addLap(65)
    thirdTrack.currentRunners[1].addLap(70)
    thirdTrack.currentRunners[1].addLap(95)
    thirdTrack.currentRunners[2].addLap(90)
    thirdTrack.currentRunners[2].addLap(95)
    thirdTrack.currentRunners[2].addLap(80)
    thirdTrack.currentRunners[2].addLap(75)
    thirdTrack.currentRunners[3].addLap(85)
    thirdTrack.currentRunners[3].addLap(85)
    thirdTrack.currentRunners[3].addLap(85)
    thirdTrack.currentRunners[3].addLap(85)
    thirdTrack.currentRunners[4].addLap(60)
    thirdTrack.currentRunners[4].addLap(95)
    thirdTrack.currentRunners[4].addLap(80)
    thirdTrack.currentRunners[4].addLap(35)
    thirdTrack.currentRunners[5].addLap(40)
    thirdTrack.currentRunners[5].addLap(55)
    thirdTrack.currentRunners[5].addLap(60)
    thirdTrack.currentRunners[5].addLap(35)


    fourthTrack = Track('Kzoo Field Track', (1/3))
    
    thirdTrack.runners[0].newSession(Session(fourthTrack))
    thirdTrack.runners[1].newSession(Session(fourthTrack))
    thirdTrack.runners[2].newSession(Session(fourthTrack))
    thirdTrack.runners[3].newSession(Session(fourthTrack))
    thirdTrack.runners[4].newSession(Session(fourthTrack))
    thirdTrack.runners[5].newSession(Session(fourthTrack))

    fourthTrack.currentRunners[0].addLap(120)
    fourthTrack.currentRunners[0].addLap(120)
    fourthTrack.currentRunners[0].addLap(120)
    fourthTrack.currentRunners[0].addLap(120)
    fourthTrack.currentRunners[1].addLap(60)
    fourthTrack.currentRunners[1].addLap(65)
    fourthTrack.currentRunners[1].addLap(70)
    fourthTrack.currentRunners[1].addLap(95)
    fourthTrack.currentRunners[2].addLap(90)
    fourthTrack.currentRunners[2].addLap(95)
    fourthTrack.currentRunners[2].addLap(80)
    fourthTrack.currentRunners[2].addLap(75)
    fourthTrack.currentRunners[3].addLap(85)
    fourthTrack.currentRunners[3].addLap(85)
    fourthTrack.currentRunners[3].addLap(85)
    fourthTrack.currentRunners[3].addLap(85)
    fourthTrack.currentRunners[4].addLap(60)
    fourthTrack.currentRunners[4].addLap(95)
    fourthTrack.currentRunners[4].addLap(80)
    fourthTrack.currentRunners[4].addLap(35)
    fourthTrack.currentRunners[5].addLap(40)
    fourthTrack.currentRunners[5].addLap(55)
    fourthTrack.currentRunners[5].addLap(60)
    fourthTrack.currentRunners[5].addLap(35)
    #secondTrack.runners[0].sessions[2].print()
    #secondTrack.runners[3].sessions[2].print()
    
    fourthTrack.runners[0].newSession(Session(fourthTrack))
    fourthTrack.runners[1].newSession(Session(fourthTrack))
    fourthTrack.runners[2].newSession(Session(fourthTrack))
    fourthTrack.runners[3].newSession(Session(fourthTrack))
    fourthTrack.runners[4].newSession(Session(fourthTrack))
    fourthTrack.runners[5].newSession(Session(fourthTrack))

    fourthTrack.currentRunners[0].addLap(110)
    fourthTrack.currentRunners[0].addLap(110)
    fourthTrack.currentRunners[0].addLap(110)
    fourthTrack.currentRunners[0].addLap(110)
    fourthTrack.currentRunners[1].addLap(50)
    fourthTrack.currentRunners[1].addLap(55)
    fourthTrack.currentRunners[1].addLap(60)
    fourthTrack.currentRunners[1].addLap(85)
    fourthTrack.currentRunners[2].addLap(80)
    fourthTrack.currentRunners[2].addLap(85)
    fourthTrack.currentRunners[2].addLap(70)
    fourthTrack.currentRunners[2].addLap(65)
    fourthTrack.currentRunners[3].addLap(75)
    fourthTrack.currentRunners[3].addLap(75)
    fourthTrack.currentRunners[3].addLap(75)
    fourthTrack.currentRunners[3].addLap(75)
    fourthTrack.currentRunners[4].addLap(50)
    fourthTrack.currentRunners[4].addLap(85)
    fourthTrack.currentRunners[4].addLap(70)
    fourthTrack.currentRunners[4].addLap(25)
    fourthTrack.currentRunners[5].addLap(30)
    fourthTrack.currentRunners[5].addLap(45)
    fourthTrack.currentRunners[5].addLap(50)
    fourthTrack.currentRunners[5].addLap(25)

    fourthTrack.runners[0].newSession(Session(fourthTrack))
    fourthTrack.runners[1].newSession(Session(fourthTrack))
    fourthTrack.runners[2].newSession(Session(fourthTrack))
    fourthTrack.runners[3].newSession(Session(fourthTrack))
    fourthTrack.runners[4].newSession(Session(fourthTrack))
    fourthTrack.runners[5].newSession(Session(fourthTrack))
    
    for i in range(len(fourthTrack.currentRunners)):
        fourthTrack.currentRunners[i].print()
        #fourthTrack.currentRunners[i].currentSession.print()
    #secondTrack.runners[0].sessions[0].print()
    
if __name__ == '__main__':
    main()
