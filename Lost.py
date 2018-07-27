import random

prob = random.random()
print("""Welcome to truth or dare.""")

truth = 1
dare = 2

td = random.randrange(1,3)
print (td)

if td == 1:
    print truth
if td == 2:
    print dare
if td == 1:
    print "Say the truth about about yourself"
if td == 2:
    print "I dare you to tell the truth about yourself"

