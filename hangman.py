import random
wlist=["ardvark","baboon","camel","german","modern"]
a=random.choice(wlist)
display=[]
size=len(a)
print("Guess the character for the following hidden word"+"\n")
'''for i in range(0,size):
    display[i]="_" '''
for c in a:
    display+="_"
print(display)

while size>0:

    guess=input("enter a letter").lower()
    n=0
    for b in a:
    
        if b==guess:
            r="right"
            display[n]=b
        
        else:
            r="wrong"
        n+=1   
    print(display)
    size-=1
w=""    
for a in display:
    w+=a
if w==a:
    print("HURAAH!! You guessed it right")
else:
    print("You failed. Try again!!")

