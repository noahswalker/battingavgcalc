
# june 11th
# fixed code hs bad indenting
# fixed code HS for loops
# took the code HS quiz, skipped the drawing questions



# fixed the indenting
# removed the question from the game interivew

# input() was broken


# correct:  input("how old are you")
# not correct:  input("how old are you", "more text")



# added a function for total at bats
# every game we asked them how many hits
# added up the totals for season hits over season at bats
# happy ending is season batting average



def start():
        #no parameters
        print("game started, welcome to my batting calculator")
        print(" ")


def askGamesPlayed():
        gamesPlayed = input("How many games did you play in this year?")
        gamesPlayed = int(gamesPlayed)
        # we have to ask, then convert to integer
        print("you were in this many games: ", gamesPlayed)
        # before we end this function
        # return the value of total games played
        return gamesPlayed

def askAboutHits(atBatsToday):
        # did you get a hit on your at bat, repeat for the at bats
        hitsThisGame = 0
        # second for loop
        for i in range(atBatsToday):
                tempString = "press 1 if you got on base, at bat #" + str(i + 1)  + " :"  
                madeHit = input(tempString)
                # convert text to integer
                madeHit = int(madeHit)
                hitsThisGame = hitsThisGame + madeHit
        return hitsThisGame
                                

def askAtBats(thisGame):
        #return a variable called
        gamesText =  str(thisGame + 1)
        print(" ")
        tempString = "how many at bats for game number " + gamesText + "? " 
        atBatsToday = input(tempString)
        atBatsToday = int(atBatsToday) 
        print(" ")
        return atBatsToday
        # extra space between games


def gameInterviews(totalGames):
        thisGame = 1
        seasonAtBats = 0
        seasonHits = 0 
        #start season at game 1
        # first for loop
        for thisGame in range(totalGames):
                #  First ask about at bats, then hits interview
                x = askAtBats(thisGame)
                y = askAboutHits(x)

                # Third is to keep track of totals all season
                seasonAtBats = seasonAtBats + x
                seasonHits = seasonHits + y
        # end of the game season
        # multply by one thousand
        # final caclulation
        seasonBattingAverage = seasonHits /  seasonAtBats
        seasonBattingAverage = seasonBattingAverage * 1000   

        print(" ")
        print("your season long at bats ", seasonAtBats)
        print(" ")
        print("your season long hits total ", seasonHits )
        print(" ")
        print("your season batting average: ", seasonBattingAverage)
        print(" ")
# end of function game interview


# this is a comment
# ask how many at bats in the first game
# hit by any pitches?
# how many hits did you get in the first game
# repeat this with a loop for the number of game
# do some math to cacluate their batting average for the season

def gameStart():
        print("This is a calculator for your batting average")
        print(" ")
        print("pres 1 for a hit, zero otherwise")


def gameOver():
        print(" ")
        print("thank  you")
        print(" ")



# this is a comment, use the pound sign at the start

seasonBattingAverage = 0
gameStart()
totalGames = askGamesPlayed()
gameInterviews(totalGames)

gameOver()


        
