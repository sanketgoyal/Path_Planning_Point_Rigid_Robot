#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pygame
import math
from sys import exit


x_i=input("Start Point: X-Coordinate")
y_i=input("Start Point: Y-oordinate")
x_f=input("Goal Point: X-Coordinate")
y_f=input("Goal Point: Y-Coordinate")


def integer_resolution(r):
    if (250%r)!=0  or(150%r)!=0:
        exit("The given resolution should be completely divisible resulting in integers")
        
r=input("An integer value for resolution is: ")
r=int(r)
integer_resolution(r)

def obstacle_space(x,y):
    q = 0
    if ((x-math.ceil(190/r))**2+math.ceil(y-(130/r))**2-math.ceil(15/r)**2)<=0:
        q=1
    if (2*x + 19*y - 1314/r <= 0) and (41*x+ 25*y -6525/r >= 0) and (y - 15/r>= 0) and (37*x +10*y - 6551/r <= 0):
        q=1
    if (38*x- 7*y - 5830/r >= 0) and (38*x + 23*y - 8530/r <= 0) and (37*x -20*y -6101/r <= 0) and (37*x +10*y - 6551/r >= 0):
        q=1
    if (x-math.floor(50/r) >= 0) and (x - math.floor(100/r) <= 0) and (y - math.floor(67.5/r) >= 0) and (y - math.floor(112.5/r) <= 0):
        q=1
    if ((x-math.ceil(140/r))/math.ceil(15/r))**2 + ((y - math.ceil(120/r))/math.ceil(6/r))**2 - 1 <=0:
        q=1
    return q

def correct_start(first_node):
    q=obstacle_space(first_node[0],first_node[1])
    if q ==1 or first_node[0] not in range(0,251) or first_node[1] not in range(0,151):
        exit("Start point inside obstacle space or outside boundary or not an integer at this resolution")
    
def correct_end(goal):
    q=obstacle_space(goal[0],goal[1])
    if q ==1 or goal[0] not in range(0,251) or goal[1] not in range(0,151):
        exit("Goal inside obstacle space or outside boundary or not an integer at this resolution")

first_node = [(float(x_i)/r), (float(y_i))/r]
correct_start(first_node)

big = []
parent = []
parent.append(first_node)
big.append(first_node)
new_index=0
z = 0
l = 0
s=0
papa = []

h = 0
h_cost = []
h_cost.append(h)


goal = [float(x_f)/r, float(y_f)/r]
correct_end(goal)

papa.append(goal)
primary_cost = float('inf')

cost = []
visited = []

new_parent = []

min_cost = 0
index = 0
cost.append(primary_cost)

def move(x,y):
    parent_X_Y = [x,y]
    right(x,y, parent_X_Y)
    left(x,y, parent_X_Y)
    up(x,y, parent_X_Y)
    down(x, y, parent_X_Y)
    up_right(x,y, parent_X_Y)
    down_right(x, y, parent_X_Y)
    up_left(x,y, parent_X_Y)
    down_left(x,y, parent_X_Y)
    
def down(x,y,parent_X_Y):
    y = y - 1
    z1 = [x,y]
    z2 = 1 + min_cost
    append(z1, z2, parent_X_Y)    

def up(x,y, parent_X_Y):
    y = y + 1
    z1 = [x,y]
    z2 = 1 + min_cost
    append(z1, z2, parent_X_Y)

def left(x,y, parent_X_Y):
    x = x-1
    z1 = [x,y]
    z2 = 1 + min_cost
    append(z1, z2, parent_X_Y)

def right(x,y, parent_X_Y):
    x = x + 1
    z1 =[x,y]
    z2 = 1 + min_cost
    append(z1, z2, parent_X_Y)
    
def up_right(x, y, parent_X_Y):
    x, y = x+1, y+1
    z1 = [x,y]
    z2 = math.sqrt(2) + min_cost
    append(z1, z2, parent_X_Y)
    
def up_left(x, y, parent_X_Y):
    x, y = x-1, y+1
    z1 =[x,y]
    z2 = math.sqrt(2) + min_cost
    append(z1, z2, parent_X_Y)
    
def down_right(x, y, parent_X_Y):
    x, y = x+1, y-1
    z1 =[x,y]
    z2 = math.sqrt(2) + min_cost
    append(z1, z2, parent_X_Y)

def down_left(x, y, parent_X_Y):
    x, y = x-1, y-1
    z1 = [x,y]
    z2 = math.sqrt(2) + min_cost
    append(z1, z2, parent_X_Y)

def heu2(z1, goal):
    h2 = math.sqrt((z1[0] - goal[0])**2 + (z1[1] - goal[1])**2) 
    return h2
    
def append(z1, z2, parent_X_Y):
    #print(goal)
    h2 = heu2(z1, goal)
    h3 = z2 + h2
    #heu(z1,z2,goal)
    q=obstacle_space(z1[0],z1[1])
    if z1[0] in range(0,int(250/r) + 1) and z1[1] in range(0,int(150/r) + 1) and q==0:       
        if z1 not in visited:
            if z1 in big:
                index1 = big.index(z1)
                h = h_cost[index1]
                if h <= h3:
                    pass
                else:
                    big.pop(index1)
                    cost.pop(index1)
                    parent.pop(index1)
                    h_cost.pop(index1)
                    cost.append(z2)
                    big.append(z1)
                    parent.append(parent_X_Y)
                    h_cost.append(h3)
            else:
                cost.append(z2)
                big.append(z1)
                parent.append(parent_X_Y)
                h_cost.append(h3)
    else:
        pass


while goal not in visited:
        move(big[new_index][0],big[new_index][1])
        visited.append(big[new_index])
        new_parent.append(parent[new_index])
        big.pop(new_index)
        cost.pop(new_index)
        parent.pop(new_index)
        h_cost.pop(new_index)
        if h_cost != []:
            min_h_cost=(min(h_cost))
            index = h_cost.index(min_h_cost)
            min_cost=cost[index]
            new_index=index
            
            
while True:
    if goal in visited:
        index3 = visited.index(goal)
        goal = new_parent[index3] 
        papa.append(goal)
        if goal == [float(x_i)/r, float(y_i)/r]:
            break

obs_space = []
for i in range(0,251):
    for j in range(0,151):
        q=obstacle_space(i,j)
        if q == 1:
            obs_space.append([i,j])




k=2
my_list = np.array(visited)
visited=my_list*k*r
my_list1 = np.array(papa)
papa=my_list1*k*r
my_list2 = np.array(obs_space)
obs_space = my_list2*k*r

pygame.init()

#Defining the colors
Black = [0, 0, 0]
Light_blue = [103, 255, 255]
Blue = [0, 0, 155]
White = [255, 255, 255]

#Height and Width of Display
SIZE = [250*k+r+r, 150*k+r+r]
screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption("A* Point")
clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:  
            done = True   
 
    screen.fill(Black)
#Printing the obstacles
    for i in obs_space:
        pygame.draw.rect(screen, Blue, [i[0],150*k-i[1],r*k,r*k])
    pygame.display.flip()
    clock.tick(20)
#Printing the visited nodes
    for i in visited:
        pygame.time.wait(1)
        pygame.draw.rect(screen, White, [i[0],150*k-i[1],r*k,r*k])
        pygame.display.flip()
#Printing the path
    for j in papa[::-1]:
        pygame.time.wait(1)
        pygame.draw.rect(screen, Light_blue, [j[0], 150*k-j[1], r*k,r*k])
        pygame.display.flip()
    pygame.display.flip()

    pygame.time.wait(15000)
    done = True
pygame.quit()


# In[ ]:





# In[ ]:




