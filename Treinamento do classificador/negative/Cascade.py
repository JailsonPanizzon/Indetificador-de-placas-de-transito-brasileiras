import urllib
from urllib.request import urlopen
import numpy as np
import cv2
import os
import subprocess
def montar_negativas():
    link_imagens_negativas = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n03215508'
    urls_imagens_negativas = urllib.request.urlopen(link_imagens_negativas).read().decode()


    if not os.path.exists('negatives'):
        os.makedirs('negatives')

    nmr_imagem=1

    for i in urls_imagens_negativas.splitlines():
        try:
            urllib.request.urlretrieve(i,str(nmr_imagem)+".jpg")
            img = cv2.imread(str(nmr_imagem)+".jpg",cv2.IMREAD_GRAYSCALE)
            img_redimin=cv2.resize(img,(640,480))
            cv2.imwrite(str(nmr_imagem)+".jpg",img_redimin)
            nmr_imagem+=1
        except Exception as e:
            print(str(e))
def gera_list_neg():
        for img in os.listdir():
            line = img+'\n'
            with open('bg.txt','a') as f:
                f.write(line)
'''def cria_amostras():
    subprocess.call(['opencv_createsamples -img 57.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 100'])
    #opencv_createsamples -info info/info.lst -num 100 -w 69 -h 69 -vec positives.vec

def treinar():
    opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 200-numNeg 100 -numStages 5 -w 69 -h 20
'''
gera_list_neg()

