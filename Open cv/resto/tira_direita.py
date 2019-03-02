import PIL
from PIL import ImageFilter
from PIL import Image


def tiradir(img):
    px = img.load()
    
    alt = img.size[0]
    larg = img.size[1]
    im2= Image.new("RGB",[690,larg],255)
    alt -=1
    larg -=1
    i=0
    while i<690:
        j=0
        while j<=larg:
            im2.putpixel([i,j],(px[i,j][0],px[i,j][1],px[i,j][2]))
            j+=1
        i+=1

    return im2
def tiraesq(img):
    px = img.load()
    
    alt = img.size[0]
    larg = img.size[1]
    im2= Image.new("RGB",[690,larg],255)
    alt -=1
    larg -=1
    i=0
    while i<690:
        j=0
        while j<=larg:
            im2.putpixel([i,j],(px[590+i,j][0],px[590+i,j][1],px[590+i,j][2]))
            j+=1
        i+=1

    return im2


def tiraesq_dir(img):
    px = img.load()
    
    alt = img.size[0]
    larg = img.size[1]
    im2= Image.new("RGB",[360,480],255)
    alt -=1
    larg -=1
    i=0
    while i<360:
        j=0
        while j<480:
            im2.putpixel([i,j],(px[360+i,j][0],px[360+i,j][1],px[360+i,j][2]))
            j+=1
        i+=1

    return im2

def tiracima_baixo(img):
    px = img.load()
    
    alt = img.size[0]
    larg = img.size[1]
    im2= Image.new("RGB",[alt,442],255)
    alt -=1
    larg -=1
    i=0
    while i<alt:
        j=0
        while j<442:
            im2.putpixel([i,j],(px[i,278+j][0],px[i,278+j][1],px[i,278+j][2]))
            j+=1
        i+=1

    return im2
i = 1
while i<7:
    nome ="f ("+str(i)+").bmp"
    img = Image.open(nome)
    img = tiraesq_dir(img)
    
    img.save((str(i)+".bmp"))
    i+=1
print("done")
