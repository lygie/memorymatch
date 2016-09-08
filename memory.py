# implementation of card game - Memory
#http://www.codeskulptor.org/#user17_gFHud4YfZY_20.py
# Weird saving issue! bottom link is finished version
#http://www.codeskulptor.org/#user17_VZXrRqAMIH_12.py
import simplegui
import random

#state = 0
#cardList1 = [str(x) for x in range(8)]
#cardList2 = [str(y) for y in range(8)]

#cardTot = cardList1 + cardList2
#random.shuffle(cardTot)
#exposed = [not x for x in range(1,17)]

# helper function to initialize globals
def init():
    global state, cardList1, cardList2, cardTot, exposed, numMoves, firstVal, secondVal, firstPos, secondPos
    cardList1 = [str(x) for x in range(8)]
    cardList2 = [str(y) for y in range(8)]
    cardTot = cardList1 + cardList2
    exposed = [not x for x in range(1,17)]
    random.shuffle(cardTot)
    numMoves = 0
    label.set_text("Moves = " + str(numMoves))
    firstVal = 0
    firstPos = 0
    secondVal = 0
    secondPos = 0
    state = 0
    
RECT_WIDTH = 50
RECT_HEIGHT = 100
numMoves = 0    

# define event handlers
def mouseclick(pos):
    global state, numMoves, firstVal, secondVal, firstPos, secondPos
    # add game state logic here
    if exposed[pos[0]//50] == True:
        pass
    else:
        if state == 0:
            state = 1
            print 'game begins'
            exposed[pos[0]//50] = True
            firstVal = cardTot[pos[0]//50]
            firstPos = pos[0]//50
            print 'firstVal is: ', firstVal
        elif state == 1: 
            #if exposed[pos[0]//50] != True:
            state = 2
            print 'state 2'
            exposed[pos[0]//50] = True
            secondVal = cardTot[pos[0]//50]
            secondPos = pos[0]//50
            print 'SecondVal is: ', secondVal
            numMoves += 1
            label.set_text("Moves = " + str(numMoves))
         
            #if firstVal == secondVal:
            exposed[firstPos] = True
            exposed[secondPos] = True
            #else:
           
             #   exposed[firstPos] = False
              #  exposed[secondPos] = False
        else:
            #this state 2 going to state 1
            state = 1
            if firstVal == secondVal:
                exposed[firstPos] = True
                exposed[secondPos] = True
            else:
                exposed[firstPos] = False
                exposed[secondPos] = False
            
            if exposed[pos[0]//50] != True:
                exposed[pos[0]//50] = True
                firstVal = cardTot[pos[0]//50]
                firstPos = pos[0]//50
            print 'firstVal is: ', firstVal
            print 'state 1'
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cardTot
    counter = 0
    for i in cardTot:
        if exposed[counter]:
            canvas.draw_text(str(i), ((counter*50+25),50),30,"Blue")
        else:
            canvas.draw_polygon([(counter*RECT_WIDTH,0), (counter*RECT_WIDTH,RECT_HEIGHT),(counter*RECT_WIDTH+50,RECT_HEIGHT),(counter*RECT_WIDTH+50,0)],1,"White", "Green")
        counter += 1


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = " + str(numMoves))

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric