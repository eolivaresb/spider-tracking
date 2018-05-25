import numpy as np
import cv2

################################ FUNCIONES A USAR ################################
def distancia(p1, p2):
    xc, yc = p1[0], p1[1]
    x, y = p2[0], p2[1]
    return np.sqrt((x - xc)**2 + (y - yc)**2)
    
def aplicar_mascara(im, poli):
    mask = np.zeros(im.shape, dtype=np.uint8)
    cv2.fillPoly(mask, poli, 255)
    # apply the mask
    return cv2.bitwise_and(im, mask)

def set_maze_length(event, x, y,flags, params):
    [aux, img, img_copy] = params
    global dist
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img_copy,(x,y),1,(255, 255, 0),-1)
        aux[0], aux[1] = x, y
    if event==cv2.EVENT_LBUTTONUP:
        aux[2], aux[3] = x, y
        cv2.circle(img_copy,(x,y),1,(255, 255, 0),-1)
        cv2.line(img_copy, tuple(aux[:2]), tuple(aux[2:]), (0, 255, 0))
    if event==cv2.EVENT_RBUTTONDOWN:
        img_copy[:]=img[:]
        aux = [0, 0, 0, 0]

def set_maze_vertices(event, x, y, flags, params):
    [cPts, overlayImage, resetImage] = params
    if event==cv2.EVENT_LBUTTONDOWN:
        cPts[0].append((x,y))
        cv2.circle(overlayImage,(x,y),5,(255),-1)
    elif event==cv2.EVENT_RBUTTONDOWN:
        cPts[0]=[]
        overlayImage[:]=resetImage[:]

def set_initial_position(event, x, y, flags, params):
    [img, img_copy, a] = params
    if event == cv2.EVENT_LBUTTONDOWN:
        print ('initial_position: '+str(x)+', '+str(y))
        cv2.circle(img_copy,(x,y),8,(255, 0, 0),-1)
        a[0] = (x, y)
    elif event==cv2.EVENT_RBUTTONDOWN:
        img_copy[:]=img[:]
        
def cortar_circulo(centro, r, img):
    imagen = np.copy(img)
    centro = np.array(centro)
    xc, yc = centro[0], centro[1]
    H, W = imagen.shape
    x, y = np.meshgrid(np.arange(W), np.arange(H))
    d2 = (x - xc)**2 + (y - yc)**2
    mask = d2 > r**2
    imagen[mask] = 255
    return imagen