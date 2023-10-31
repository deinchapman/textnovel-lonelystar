intro = """
Once again,
you,
the "Mortificado",
a being that has experience nothing else but suffer in his life,
has once again experienced a new calamity.
At this point...
you just want to go to your especial place;
...and talk with the only being that you feel that listens to you...
"""

text1v1 = """
Today you went out to look for the moon as you always do.
You only wish to the least being able to delight yourself with it's beauty.
"""

text2v1 = """
While you try to look at the sky,
it seems that you cannot be able to find the moon by nowhere you try to look at;
nevertheless... the one thing you could find is a lonely star,
that only because of it's lonliness you let yourself notice it's poor shine.
"""

endingSimp = """
You just ignored the star,
and went on to keep looking for the moon,
no matter how much it does cost you to find it,
even if you've lost yourself,
you'll keep chase her for forever.


Ending S: [S]imp walking
"""

text1v2 = """
The Lonely Star answers to your shouts with another question: 
- I'm the one who wants to ask,"Moritificado";
Is it worth go looking for it? -
"""

text2v2 = """
- Just try to call and shout her name,
I just wanna let you know that if nobody answers,
it's because nobody cares -")
"""

text3v2 = """
- If you ask "me" a lonely star,
The moon didn't gave you anything back.
The moon is not worth the effort it's my conclusion,
"Mortificado" my friend...
Never mind it's beauty,
if you were to go chasing behind her,
you'd be at garbage time -


Ending R: [R]eality Check"
"""

print(intro)
print()
answer = input("press enter to continue:")
if answer == 1: 
    print(text1v1) 
    
else:
    print(text1v1)
    
answer = input("press enter to continue:")
if(1):
    print(text2v1)
else:
    print(text2v1)

while True:
    try:    
        answer = input("Try to shout at the star where can you find the moon? (yes/no):")

        if answer.lower() == "no":
            print(endingSimp)
            exit()
        
        elif answer.lower() == "yes":
            print(text1v2)
            break
              
    except Exception:
        print("Invalid input")
    continue

answer = input("press enter to continue:")
if(1):
    print(text2v2)
else:
    print(text2v2)
        
answer = input("press enter to continue:")
if(1):
    print(text3v2)
else:
    print(text3v2)
