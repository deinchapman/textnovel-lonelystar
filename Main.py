intro = ("\nOnce again,\nyou,\nthe \"Mortificado\",\na being that has experience nothing else but suffer in his life,\nhas once again experienced a new calamity.\nAt this point...\nyou just want to go to your especial place;\n...and talk with the only being that you feel that listens to you...\n")

text1v1 = ("\nToday you went out to look for the moon as you always do.\nYou only wish to the least being able to delight yourself with it's beauty.\n")

text2v1 = ("\nWhile you try to look at the sky,\nit seems that you cannot be able to find the moon by nowhere you try to look at;\nnevertheless... the one thing you could find is a lonely star,\nthat only because of it's lonliness you let yourself notice it's poor shine.\n")

endingSimp = ("\nYou just ignored the star,\nand went on to keep looking for the moon,\nno matter how much it does cost you to find it,\neven if you've lost yourself,\nyou'll keep chase her for forever.\n \n \n Ending S: [S]imp walking")

text1v2 = ('\nThe Lonely Star answers to your shouts with another question: \n- I\'m the one who wants to ask,\n"Moritificado";\nIs it worth go looking for it? -\n')
               
text2v2 = ("\n- Just try to call and shout her name,\nI just wanna let you know that if nobody answers,\nit's because nobody cares -\n")

text3v2 = ("\n- If you ask \"me\" a lonely star,\nThe moon didn't gave you anything back.\nThe moon is not worth the effort it's my conclusion,\n\"Mortificado\" my friend...\nNever mind it's beauty,\nif you were to go chasing behind her,\nyou'd be at garbage time -\n \n \n Ending R: [R]eality Check")

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


    
    

    
    
    
    
    


