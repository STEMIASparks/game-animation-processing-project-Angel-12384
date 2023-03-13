top_left = 0 # 0-empty,1-X,2-O
top_right =0# 0-empty,1-X,2-O
top_middle = 0# 0-empty,1-X,2-O

middle_left = 0# 0-empty,1-X,2-O
middle_right = 0# 0-empty,1-X,2-O
middle_middle =0# 0-empty,1-X,2-O

bottom_left =0# 0-empty,1-X,2-O
bottom_right =0# 0-empty,1-X,2-O
bottom_middle =0 # 0-empty,1-X,2-O

turn = 1

def setup ():
    size(500,500)
    background(255,255,255)
    
def draw ():
   # drawing game board
     strokeWeight(4)
     stroke(0,0,400)
     line(150,0,150,500)
     line(330,0,330,500)
     line(0,150,900,150)
     line(0,350,900,350)
     # top left O
     if top_left == 2:
        fill(255,255,0)
        ellipse(70,70,100,100)
     # top left X
     fill(0,0,400)
     if top_left ==1:
        line(0,0,150,150)
        line(150,0,0,150)
     # top middle O
     if top_middle ==2:
        fill(255,255,0)
        ellipse(240,70,100,100)
     # top middle X
     elif top_middle ==1:
        line(330,0,150,150)
        line(150,0,330,150)
     # top right O
     if top_right ==2:
        fill(255,255,0)
        ellipse(430,70,100,100)
     # top right X
     elif top_right ==1:
        line(500,0,330,150)
        line(330,0,500,150)
     # middle left 0
     if middle_left ==2:
        fill(255,255,0)
        ellipse(70,250,100,100)
     # middle left X
     elif middle_left ==1:
        line(0,340,150,150)
        line(150,340,0,150)
     # middle middle 0
     if middle_middle == 2:
         fill(255,255,0)
         ellipse(250,250,100,100)
      # middle middle X
     elif middle_middle ==1:
        line(150,150,330,330)
        line(330,150,150,330)
     # middle right 0 
     if middle_right ==2:
        fill(255,255,0)
        ellipse(430,250,100,100)
     # middle right X
     elif middle_right==1:
        line(500,150,330,345)
        line(330,150,500,330)
     # bottom left 0
     if bottom_left==2:
        fill(255,255,0)
        ellipse(70,430,100,100)
     # bottom left X
     elif bottom_left ==1:
        line(0,500,145,345)
        line(145,500,0,345)
     # bottom middle 0
     if bottom_middle ==2:
        fill(255,255,0)
        ellipse(250,430,100,100)
     # bottom middle X
     elif bottom_middle ==1:
        line(150,500,330,345)
        line(330,500,150,345)
     # bottom right 0
     if bottom_right ==2:
        fill(255,255,0)
        ellipse(430,430,100,100)
     # bottom right X
     elif bottom_right ==1:
        line(500,500,345,345)
        line(345,500,500,345)
        
def mousePressed ():
    println([mouseX,mouseY])
    global top_left
    global top_middle
    global top_right
    
    global middle_left
    global middle_middle
    global middle_right
    
    global bottom_left
    global bottom_middle
    global bottom_right
    global turn
    
    if (mouseX > 0 and mouseX < 200) and (mouseY > 0 and mouseY < 200 ):
        top_left = turn
        
        # switch turns
        if turn == 1:
            turn = 2
        elif turn ==2:
            turn = 1
        
    elif(mouseX > 150 and mouseX < 330) and (mouseY > 0 and mouseY< 150):
        top_middle = turn
        
         # switch turns
        if turn == 1:
            turn = 2
        elif turn ==2:
            turn = 1
            
    elif(mouseX > 330 and mouseX < 500) and (mouseY > 0 and mouseY < 150) :
        top_right = turn
        
          # switch turns
        if turn == 1:
            turn = 2
        elif turn ==2:
            turn = 1
        
        
    elif(mouseX > 0 and mouseX < 150) and (mouseY > 150 and mouseY < 340):
        middle_left = turn
        
         # switch turns
        if turn == 1:
            turn = 2
        elif turn ==2:
            turn = 1
            
    elif(mouseX >150 and mouseX < 350) and (mouseY > 150 and mouseY< 350) :
        middle_middle = turn
         
         # switch turns
        if turn == 1:
            turn = 2
        elif turn ==2:
            turn = 1
        
    elif(mouseX > 330 and mouseX < 500) and (mouseY > 150 and mouseY < 350):
        middle_right = turn
        
         # switch turns
        if turn == 1:
            turn = 2
        elif turn ==2:
            turn = 1
       
         
    elif(mouseX > 0 and mouseX < 150) and (mouseY > 345 and mouseY < 500):
        bottom_left = turn 
       
         # switch turns
        if turn == 1:
            turn = 2
        elif turn ==2:
            turn = 1
        
    elif(mouseX > 150 and mouseX < 330) and (mouseY > 345 and mouseY< 500):
        bottom_middle = turn
        
         # switch turns
        if turn == 1:
            turn = 2
        elif turn ==2:
            turn = 1
       
    elif(mouseX > 330 and mouseX < 500) and (mouseY > 330 and mouseY < 500):
        bottom_right = turn
        
         # switch turns
        if turn == 1:
            turn = 2
        elif turn ==2:
            turn = 1
    # check for winners
    if middle_left ==1 and middle_middle ==1 and middle_right==1:
        print("winner! middle row 1")
    elif middle_left == 2 and middle_middle ==2 and middle_right==2:
        print("winner! middle row 2")
    if top_left == 1 and top_middle == 1 and top_right == 1:
        print(" winner! top row 1")
    elif top_left == 2 and top_middle == 2 and top_right == 2:
        print(" winner! top row 2")
    if  bottom_left ==1 and bottom_middle == 1 and bottom_right ==1:
        print(" winner! bottom row 1")
    elif bottom_left == 2 and bottom_middle == 2 and bottom_right ==2:
        print("winner! bottom row 2")
    if top_left ==1 and middle_left ==1 and bottom_left == 1:
        print("winner! left column 1")
    elif top_left ==2 and middle_left ==2 and bottom_left == 2:  
        print("winner! left column 2")
    if  top_middle ==1 and middle_middle ==1 and bottom_middle == 1:
        print("winner! middle column 1")
    elif top_middle ==2 and middle_middle ==2 and bottom_middle ==2:
        print("winner! right column 2")
    if top_right ==1 and middle_middle == 1 and bottom_left == 1:
        print(" winner! diagonal towards the right 1")
    
    
    
            
   
     

   
     
     
     

     
