import cv2
import time
import numpy as np
import os
import PIL
import math
def equaliza(img):
    b, g, r = cv2.split(img)
    red = cv2.equalizeHist(r)
    green = cv2.equalizeHist(g)
    blue = cv2.equalizeHist(b)
    blue=b
    return cv2.merge((blue, green, red))

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

placa = cv2.CascadeClassifier('boards.xml')
cap = cv2.VideoCapture("VID_20180917_180839_1.avi")
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
while True:
    find = False
    ret, img = cap.read()
    #img = equaliza(img)
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    i = 1
    cv2.imwrite("teste.jpg", gray)
    gra = cv2.imread("teste.jpg")
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
    board = placa.detectMultiScale(gray, 1.9,4)
    

    for (x,y,w,h) in board:
        find = True
        cv2.rectangle(gray , (x,y),(x+w, y+h), (255,0,0),2)
        print("placa")
    cv2.imshow('img',gray)
    k=cv2.waitKey(30) & 0xff
    
    if find:
        print(board)
        val = input("certa(1) ou errada(2):\n")
        if(val == '1'):
           cv2.imwrite("Right/"+str(right)+".jpg",gray)
           right+=1
        else:
           gra = cv2.imread("teste.jpg")
           corte = gra[board[0][1]:board[0][1]+board[0][3],board[0][0]:board[0][0]+board[0][2]]
           cv2.imshow('crop', corte)
           corte = cv2.resize(gra,(640,480))
           cv2.imwrite("wrong/"+str(wrong)+".jpg",corte)
           wrong+=1
    else:
        cv2.imwrite("resto/"+str(num)+".bmp",gray)
        num+=1   

    if k == 27:
        break

cap.realese()
cv2.destroyAllWindows
