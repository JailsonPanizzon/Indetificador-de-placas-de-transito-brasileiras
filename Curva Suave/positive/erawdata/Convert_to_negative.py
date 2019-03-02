import PIL
import tkinter
from tkinter import *
import PIL
from PIL import ImageFilter
from PIL import Image
import math
import cv2

def negative(img):
    img = img.resize((640,480),Image.ANTIALIAS)
    img = niveis_de_cinza(img)
    return img
    

def niveis_de_cinza(im):
    
    im2 = Image.new('L',im.size,0)
    px = im.load()
    opcao = True
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            media = ((px[i,j][0])+(px[i,j][1])+(px[i,j][2]))//3
            if opcao:
                if media> 10 and media<=20:
                    im2.putpixel([i,j],15)
                elif media> 20 and media<=30:
                    im2.putpixel([i,j],25)
                elif media> 30 and media<=40:
                    im2.putpixel([i,j],35)
                elif media> 40 and media<=50:
                    im2.putpixel([i,j],45)
                elif media> 50 and media<=60:
                    im2.putpixel([i,j],55)
                elif media> 60 and media<=70:
                    im2.putpixel([i,j],65)
                elif media> 70 and media<=80:
                    im2.putpixel([i,j],75)
                elif media> 80 and media<=90:
                    im2.putpixel([i,j],85)
                elif media> 90 and media<=100:
                    im2.putpixel([i,j],95)
                elif media> 100 and media<=110:
                    im2.putpixel([i,j],105)
                elif media> 110 and media<=120:
                    im2.putpixel([i,j],115)
                elif media> 120 and media<=130:
                    im2.putpixel([i,j],125)
                elif media> 130 and media<=140:
                    im2.putpixel([i,j],135)
                elif media> 140 and media<=150:
                    im2.putpixel([i,j],145)
                elif media> 150 and media<=160:
                    im2.putpixel([i,j],155)
                elif media> 160 and media<=170:
                    im2.putpixel([i,j],165)
                elif media> 170 and media<=180:
                    im2.putpixel([i,j],175)
                elif media> 180 and media<=190:
                    im2.putpixel([i,j],185)
                elif media> 190 and media<=200:
                    im2.putpixel([i,j],195)
                elif media> 200 and media<=210:
                    im2.putpixel([i,j],205)
                elif media> 210 and media<=220:
                    im2.putpixel([i,j],215)
                elif media> 220 and media<=230:
                    im2.putpixel([i,j],225)
                elif media> 230 and media<=240:
                    im2.putpixel([i,j],235)
                elif media> 240 and media<=250:
                    im2.putpixel([i,j],245)
                elif media> 250 and media<=260:
                    im2.putpixel([i,j],255)
                elif media<10:
                    im2.putpixel([i,j],0)
            else:
                if media>170:
                    im2.putpixel([i,j],255)
                else:
                    im2.putpixel([i,j],0)

    return im2
i=1
while i<200:
    nome = "r ("+str(i)+").jpg"
    im = Image.open(nome)
    #im = negative(im)
    im.save(str(i+61)+".bmp")

    i+=1
