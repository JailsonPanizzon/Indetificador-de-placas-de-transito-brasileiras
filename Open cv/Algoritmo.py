import colorsys

import cv2
import time
import numpy as np
import os
import PIL
import math
import time

from PIL import Image


def convert(rgb):
    hsv=colorsys.rgb_to_hsv(rgb[0],rgb[1],rgb[2])
    return hsv


def equaliza(img):
    #equaliza imagens nos canais R,G,B
    b, g, r = cv2.split(img)
    red = cv2.equalizeHist(r)
    green = cv2.equalizeHist(g)
    blue = cv2.equalizeHist(b)
    blue=b
    return cv2.merge((blue, green, red))

def day_or_night(im):
    px=im.load()    
    j=im.size[1]-1
    soma=0
    while(j>=0):
        i=0
        while(i<im.size[0]-1):
            ij=convert(px[i,j])
            soma+=ij[2]
            i+=10
        j-=10
    soma=soma//((im.size[0]*im.size[1])/100)
    if(soma >60):
        print("day")
    else:
        print("night")
    return soma

def teste(img):
    b, g, r = cv2.split(img)
    i=0
    while i < len(r):
        j=0
        while j < len(r):
            distancia=math.sqrt((pow((r[i][j])-255,2)+pow((g[i][j])-235,2)+pow((b[i][j])-0,2)))
            if(distancia< 100):
                r[i][j]=255
                g[i][j]=255
                b[i][j]=0
            j+=1
        i+=1
    return cv2.merge((r, g, b))



#Abra arquivo XML com as features de reconhecimento
placa = cv2.CascadeClassifier('placacascade3.xml')
#seleciona o video de entrada
cap = cv2.VideoCapture("video noite.avi")
right = 0
wrong = 71
num = 0
mask = [[-1, 1, -1],
        [ 1, 2, 1],
        [-1, 1, -1]]
if not(os.path.isdir('./right')):
    os.mkdir('./Right')
if not(os.path.isdir('./wrong')):
    os.mkdir('./wrong')
if not(os.path.isdir('./resto')):
    os.mkdir('./resto')
#loop para aplicar o identificador em cada frame    
while True:
    find = False
    #dicionario para salvar o frame em uma imagem
    ret, img = cap.read()
    cv2.imwrite("teste.jpg", img)
    im = Image.open("teste.jpg")
    t = day_or_night(im)
    img2 = img[int(img.shape[0]*0.3):img.shape[0],int(img.shape[1]*0.5):img.shape[1]]
    img2 = equaliza(img2)
    gray = cv2.cvtColor(img2 , cv2.COLOR_BGR2GRAY)
    i = 1
    '''#detecção de bordas
    while(i < gray.shape[0]-1):
        j = 1
        while(j<gray.shape[1]-1):
              print(gra[i][j])
              soma = (gra[i-1,j-1]*mask[0][0])
              soma += (gray[i-1,j]*mask[0][1])
              soma += (gray[i-1,j+1]*mask[0][2])
              soma += (gray[i,j-1]*mask[1][0])
              soma += (gray[i,j]*mask[1][1])
              soma += (gray[i,j+1]*mask[1][2])
              soma += (gray[i+1,j-1]*mask[2][0])
              soma += (gray[i+1,j]*mask[2][1])
              soma += (gray[i+1,j+1]*mask[2][2])
              gra[i,j] = soma  
              j+=1
        print(i)
        i+=1
    '''
    cv2.imshow("after", img)
    #aplica o classificador na imagem em tons de cinza e equalida
    board = placa.detectMultiScale(gray, 1.9,5)
    
    #desenha um retangulo tendo como base os pontos salvos no comando anterior no vetor board
    for (x,y,w,h) in board:
        find = True
        cv2.rectangle(gray , (x,y),(x+w, y+h), (255,0,0),2)
        print("placa")
    #mostra a imagem com o retangulo desenhado
    cv2.imshow('img',gray)
    k=cv2.waitKey(30) & 0xff
    if(find):
        time.sleep(2)   

    if k == 27:
        break

cap.realese()
cv2.destroyAllWindows
