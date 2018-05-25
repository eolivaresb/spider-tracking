## Script developed to get the position of a spider in a maze.
## The


import numpy as np
import os
import cv2
from tracking_aux import *

####################################################
###### PARAMETROS PARA CADA VIDEO A ANALIZAR  ######
####################################################
cam = cv2.VideoCapture('test.avi')
threshold = 12

img = cam.read()[1]
height , width , layers =  img.shape
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video = cv2.VideoWriter('tracking.avi',fourcc,20,(width,height))

####################################################
########### INDICAR DIMENSIONES DEL LABERINTO ######
####################################################
for i in range(1): img = cam.read()[1]
#cv2.namedWindow('Define the maze length in pixels')
#img_copy = np.copy(img)
#aux = [0, 0, 0, 0]
#cv2.setMouseCallback('Define the maze length in pixels', set_maze_length, [aux, img, img_copy])
#while True:
#    cv2.imshow('Define the maze length in pixels', img_copy)
#    key = cv2.waitKey(5)
#    if key == 27:
#        cv2.destroyAllWindows()
#        break
#dist = distancia(aux[:2], aux[2:])
#print(dist)
#np.savetxt('distancia', [dist])
#
###########################################################
##### INDICAR CON MOUSE POSICION INICIAL DE LA ARANHA #####
###########################################################
#cv2.namedWindow('Define spider initial location')
#a = [[]]
#img_copy = np.copy(img)
#cv2.setMouseCallback('Define spider initial location', set_initial_position, [img, img_copy, a])
#while True:
#    cv2.imshow('Define spider initial location', img_copy)
#    key = cv2.waitKey(5)
#    if key == 27: # Esc key
#        cv2.destroyAllWindows()
#        break
#a = tuple(a[0])

##########################################################
######## DEFINIR CONTORNO DEL LABERINTO ##################
##########################################################
image1 = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
image2 = np.copy(image1)

cv2.namedWindow('Define maze edges')
cPts=[[]]
cv2.setMouseCallback('Define maze edges',set_maze_vertices, [cPts, image2, image1])
opacity=0.4
while True:
    displayImage=cv2.addWeighted(image2,opacity,image1,1-opacity,0)
    cv2.imshow('Define maze edges',displayImage)
    key =cv2.waitKey(5)
    if key == 27:
        break
    elif key == 32: #Bar key
        poli = np.array(cPts, dtype=np.int32)
        t_plus = aplicar_mascara(cv2.cvtColor(cam.read()[1], cv2.COLOR_RGB2GRAY), poli)
        cv2.imshow('laberinto',t_plus)
        np.savetxt('poli', cPts[0])
cv2.destroyAllWindows()

###########################################################
############### TRACKING DEL ANIMAL #######################
###########################################################
#cv2.namedWindow('tracking')
#
#t_minus = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#img = cam.read()[1]
#t_plus = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#
#frame = 3
#cambios_ant = np.array([0, 0])
#empezar = 0
#
#centro = np.array(a)
#trayectoria = centro
#print (trayectoria)
#
#while True:
#    t_minus_v = cortar_circulo(a, 100, t_minus)
#    t_minus_v = aplicar_mascara(t_minus_v, poli)
#    t_plus_v = cortar_circulo(a, 100, t_plus)
#    t_plus_v = aplicar_mascara(t_plus_v, poli)
#
#
#    dif = cv2.absdiff(t_plus_v, t_minus_v)
#    dif = cv2.medianBlur(dif,5)
#    if np.max(dif) > threshold:
#        cambios = np.where(dif >= threshold)
##        print cambios
#        dif *= 0
#        dif[cambios] = 255
#        dif[cambios_ant] = 0
#        cambios_ant = cambios
#        centro = ( (int(np.mean(cambios[1])) ,int(np.mean(cambios[0]))))
#        a = tuple(centro)
#    trayectoria = np.c_[trayectoria, centro]
#
#    show = img
#    cv2.circle(show, a, 3, (0, 255, 0), thickness=2)
#    cv2.circle(show, a, 30, (255, 0, 0), thickness=2)
#    
#    cv2.imshow('tracking', show)
#    video.write(show)
#    t_minus = t_plus
#
#    try:
#        img = cam.read()[1]
#        t_plus = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
#    except:
#        break
#
##Bar key start the analysis
#    if empezar == 0:
#        key = cv2.waitKey(0)
#        if key == 32:
#            empezar = 1
#
##Print frame number if Bar key is pressed, exit if Esc key is pressed.
#    key = cv2.waitKey(1)
#    if key == 32:
#        print (frame)
#    elif key == 27:
#        cv2.destroyWindow('tracking')
#        break
#    
#    frame += 1
#
#video.release()
#np.savetxt('trayectoria', trayectoria)
#os.system('python plot_results.py')



