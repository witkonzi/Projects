import pygame
import math
import numpy 

pygame.init()

def screen_size(screen_width,screen_height):
    return(screen_width,screen_height)

resolution_of_window=screen_size(1366,768)
running_process=True
value_for_sin_x=0
clock=pygame.time.Clock()
window=pygame.display.set_mode((resolution_of_window[0],resolution_of_window[1]))
pygame.display.set_caption("Rotating cube!")

points=[]
points.append(numpy.matrix([-1,1,1]))
points.append(numpy.matrix([-1,1,-1]))
points.append(numpy.matrix([-1,-1,-1]))
points.append(numpy.matrix([1,-1,-1]))
points.append(numpy.matrix([1,-1,1]))
points.append(numpy.matrix([1,1,-1]))
points.append(numpy.matrix([1,1,1]))
points.append(numpy.matrix([-1,-1,1]))

projection_matrix=numpy.matrix([
  [1 , 0 , 0],
  [0 , 1 , 0]  
])
projected_points=[
    [n,n] for n in range(len(points))
]

def connecting_points(i,j,points):
    pygame.draw.line(window,"Black",(points[i][0],points[i][1]),(points[j][0],points[j][1]))
scale=100
circle_pos=[resolution_of_window[0]/2,resolution_of_window[1]/2] #x,y
angle=0

while running_process:
    clock.tick(60)
    value_for_sin_x+=0.01
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_process=False
    window.fill("White")

    angle+=0.01
    
    rotation_x=numpy.matrix([
        [1 , 0 , 0],
        [0 , math.cos(angle) , math.sin(-angle)],
        [0 , math.sin(angle) , math.cos(angle)]
    ])
    rotation_y=numpy.matrix([
        [math.cos(angle) , 0 , math.sin(angle)],
        [0 , 1 , 0],
        [math.sin(-angle) , 0 , math.cos(angle)]
    ])
    rotation_z=numpy.matrix([
        [math.cos(angle) , math.sin(-angle) , 0],
        [math.sin(angle) , math.cos(angle) , 0],
        [0 , 0 , 1]
    ])

    i=0
    for point in points:
        rotated_2d=numpy.dot(rotation_z,point.reshape((3,1)))
        rotated_2d=numpy.dot(rotation_y,rotated_2d)
        rotated_2d=numpy.dot(rotation_x,rotated_2d)
        
        projection_2d=numpy.dot(projection_matrix, rotated_2d)
        
        x=int(projection_2d[0][0] * scale) + circle_pos[0]
        y=int(projection_2d[1][0] * scale) + circle_pos[1]
        projected_points[i]=[x,y]
        pygame.draw.circle(window,"Black",(x,y),5)
        i+=1
    connecting_points(0,1,projected_points)
    connecting_points(1,2,projected_points)
    connecting_points(2,3,projected_points)
    connecting_points(3,4,projected_points)
    
    connecting_points(1,5,projected_points)
    connecting_points(4,6,projected_points)
    connecting_points(7,0,projected_points)
    connecting_points(5,3,projected_points)
    
    connecting_points(4,7,projected_points)
    connecting_points(6,5,projected_points)
    connecting_points(2,7,projected_points)
    connecting_points(0,6,projected_points)
    
    connecting_points(7,5,projected_points)
    connecting_points(6,2,projected_points)
    connecting_points(4,1,projected_points)
    connecting_points(0,3,projected_points)
    
    pygame.display.update()
    
    

    
    
    