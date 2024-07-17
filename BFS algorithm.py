import time


class CActor:
    x=0 #postion of the square in x-axis
    y=0 #postion of the square in y-axis
    ht=70 #height of the square
    wd=70 #width of the square
    type=0 # type 0 for normal square - 1 for start and end squares -
    row=-1
    coloum=-1

# Importing the library

import pygame
import sys
clock = pygame.time.Clock()

#check if the node is visited
def visited_Node_check(node):
    global visited

    for x in visited:
        if node == x:
            print(node.row, ",", node.coloum, " Visited Cell ")

            return True
    return False


def drawing_Game():
    # Drawing Squares
    for x in largeList:
        for i in range(n):
            if x[i].type == 0:
                pygame.draw.rect(surface, normal_color, pygame.Rect(x[i].x, x[i].y, x[i].wd - 2, x[i].ht - 2))
            elif x[i].type == 1:
                pygame.draw.rect(surface, startAndend_color, pygame.Rect(x[i].x, x[i].y, x[i].wd - 2, x[i].ht - 2))
            else:
                pygame.draw.rect(surface, visited_node_color, pygame.Rect(x[i].x, x[i].y, x[i].wd - 2, x[i].ht - 2))

    pygame.display.flip()



def BFS():
    start_time=time.time()

    global fringe
    while True:
        current_node=fringe.pop(0)
        print(current_node.row , ",",current_node.coloum)
        if(current_node==largeList[end_r][end_c]):

            print(current_node.row , ",",current_node.coloum , "Goal Cell")
            print("lenth of visited is ",len(visited))
            print("found goal")
            print("time elapsed:{:.2f}s".format(time.time()-start_time))
            return True
            break
        if visited_Node_check(current_node)==True:
            continue
        expand_Node(current_node)
        visited.append(largeList[current_node.row][current_node.coloum])
        largeList[current_node.row][current_node.coloum].type=3
        drawing_Game()
        clock.tick(1)


#it works clockwise
def expand_Node(node):
    global fringe

    #check left
    if (node.row > 0):
        if (visited_Node_check(largeList[node.row - 1][node.coloum]) == False):
            fringe.append(largeList[node.row - 1][node.coloum])

    #check down
    if (node.coloum < n-1):
        if (visited_Node_check(largeList[node.row][node.coloum + 1]) == False):
            fringe.append(largeList[node.row][node.coloum + 1])

    #check right
    if (node.row < n-1):
        if (visited_Node_check(largeList[node.row + 1][node.coloum]) == False):
            fringe.append(largeList[node.row + 1][node.coloum])

    #check up
    if(node.coloum>0):
        if (visited_Node_check(largeList[node.row][node.coloum-1]) == False):
            fringe.append(largeList[node.row][node.coloum-1])





n=5
thisList=[]
largeList=[]
# creating the 2D List of objects from type CActor
for r in range(n):
    for c in range(n):
        act = CActor()

        act.x= act.x + ( c * act.wd)
        act.y= act.y + ( r * act.ht)
        act.row = r
        act.coloum = c

        thisList.append(act)


    largeList.append(thisList)
    thisList = []


# Initializing Pygame
pygame.init()
SCREEN_HEIGHT = 350
SCREEN_WIDTH = 350


# Initializing surface
surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # size of the window


# Initialing Color
normal_color = (100, 88, 99)
startAndend_color = (255,0,0)
visited_node_color=(0, 255, 0)


#custom varibale
fringe=[]
visited=[]
start_r=0
start_c=0
end_r=0
end_c=0
ctClicks=0


# infinite loop to display the game
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        # check if user click the mouse button and we use it to know the Start and End of search
        if event.type == pygame.MOUSEBUTTONDOWN:
            # the user have only two clicks one for Start and the second one for End


                # check if user click the mouse button in the area of the board not outside
                if pygame.mouse.get_pos()[1] < n*70 and pygame.mouse.get_pos()[0] < n*70:
                    ctClicks += 1
                    if ctClicks == 2:
                        if BFS() == True:
                            break
                    # tring to find the selected square that the user clicked on it and change its type to 1
                    for r in range(len(largeList)):
                        for c in range(n):
                            if pygame.mouse.get_pos()[0] > largeList[r][c].x and pygame.mouse.get_pos()[0] < \
                                    largeList[r][c].x + largeList[r][c].wd and pygame.mouse.get_pos()[1] > largeList[r][
                                c].y and pygame.mouse.get_pos()[1] < largeList[r][c].y + largeList[r][c].ht:
                                largeList[r][c].type = 1
                                if ctClicks == 1:
                                    start_r = 0
                                    start_c = 0
                                    end_r = r
                                    end_c = c
                                    fringe.append(largeList[start_r][start_c])




    # Drawing Squares
    drawing_Game()
















