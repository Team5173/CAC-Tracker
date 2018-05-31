from track import *

def main():
    CACtracker = tracker()
    CACtracker.addTrack('CAC', (1/8))
    runner = Runner( 120, 6, 'F', 'Joey', 000)
    CACtracker.addRunner(runner)
    #CACtracker.print()
    CACtracker.tracks[0].addCurrentRunner(runner)
    runner.addLap(60)
    CACtracker.print()



if __name__ == '__main__':
    main()


