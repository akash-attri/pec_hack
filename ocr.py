from pytesser import *
import PIL
from PIL import Image

basewidth=200
img = Image.open("file1.png")
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
img.save('file1.png')
#######
img.close()
img2 = Image.open("file1.png")
#######
text = image_to_string(img2)
print "file converted text obtained = ",text,type(text)
f1=open("D:\Projects\hackathon\content2.txt","w")
print "recognized text written to file , content = ",text,type(text)
f1.write(text)
print "written to file"
print text
print "written done"
f1.close()
img2.close()
print "ending module"



