import random

prob = random.random()

ans1 = ("An exciting adventure awaits you.")
ans2 = ("Don't wait for success to come - go find it!")
ans3 = ("One thing about stars is that they or it ends up with a bang.")
ans4 = ("You will be the best at fortnite gaming....later. :)")
ans5 = ("Laugh a lot to live long. :)")
ans6 = ("You will be a star.")
ans7 = ("Don't wait for success to come - go find it!")
ans8 = ("Your fairy tail dreams will come true.....maybe. :)")
ans9 = ("An advice, the wise one speakes because he has too, the foul because he choose too.")
ans10 = ("When the earth is invaded by aliens you will be her hero.")
ans11 = ("Magic can't work on you.")
ans12 = ("Laugh a lot to live long. :)")
ans13 = ("Trust your friends, but keep your eyes open.")
ans14 = ("You are going to fall for someone who is the best of your type.")
ans15 = ("Everything has beauty, but not everyone can see it. :)")
ans16 = ("Your life will be good, good and good. :)")
ans17 = ("Fame and fortune lie ahead.")
ans18 = ("You will get free games by the end of this year.")
ans19 = ("Fame and fortune lie ahead.")
ans20 = ("To achieve wisdom, you must first desire it.")
ans21 = ("To achieve wisdom, you must first desire it.")
ans22 = ("Free your mind, and the rest will follow.")
ans23 = ("The next multiplayer game you will play, you will win!!! :)")
ans24 = ("The next multiplayer game you will play, you will loose. :|")
ans25 = ("You could likely inherit a large sum of money.")
ans26 = ("Your next birthday party will be awesome. :)")
ans27 = ("Everything is cool when your part of a team.")
ans28 = ("An advice, everything is awesome, when you're living out a dream.")
ans29 = ("Pursue your dreams with strength and good health.")
ans30 = ("everything is cool when your part of a team.")

Mlist = [ans1,ans2,ans3,ans4,ans9,ans10,ans13,ans14,ans17,ans18,ans21,ans23,ans24,ans27,ans28]
Flist = [ans6,ans5,ans7,ans8,ans11,ans12,ans15,ans16,ans19,ans20,ans22,ans25,ans26,ans29,ans30]

ans = raw_input("Do you need a little bit of future advice or fortune telling?Y or N")
if ans.lower() == "y":
    choice = raw_input("(Are you a male = M or female = F). M or F")
    if  choice.lower() == "m":
        M = random.randrange(0,14)
        choice1 = Mlist[M]
        print choice1
    elif choice.lower() == "f":
        F = random.randrange(0,14)
        choice2 = Flist[F]
        print choice2
else:
    print("You're loss :(")
    





