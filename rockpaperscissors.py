import random

prob = random.random()



rock = 1
papper = 2
scissors = 3
lizard = 4
spock = 5

rpsls = random.randrange(1,6)
print (rpsls)

if rpsls == 1:
    print "rock"
if rpsls == 2:
    print "papper"
if rpsls == 3:
    print "scissors"
if rpsls == 4:
    print "lizard"
if rpsls == 5:
    print "spock"