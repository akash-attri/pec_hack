
import os
#import time
#####################################
parameter=3000
#####################################
print "initialising"
os.system("ping 127.0.0.1 -n 6 > nul")
print "running"
file1="file1.png"

file2="file2.png"
try:
    os.system("del file1.png")
    os.system("c > file1.png")
except:
    os.system("c > file1.png")
    
try:
    os.system("del file2.png")
    os.system("c > file2.png")
except:
    os.system("c > file2.png")


alternate=0


def best_match(x,y,parameter):
    s1=os.stat(x).st_size
    print s1
    s2=os.stat(y).st_size
    print s2
    if s1==0 and s2==0:
        return 0
    if abs(s1-s2)<parameter:
        return 1
    return 0


while not best_match(file1,file2,parameter):
    
    print "no still image"
    if alternate==0:
        os.system("screen.bat file1.png")
        alternate=1-alternate
        
    else:
        os.system("screen.bat file2.png")
        alternate=1-alternate
    
    
    #time.(1)##delay 2 second
    os.system("ping 127.0.0.1 -n 0 > nul")

print "still image obtained"


#from recognize import *

#s=convert()
os.system("D:\Projects\hackathon\ocr.py")
#execfile(r"D:\Projects\hackathon\ocr.py")
f=open("D:\Projects\hackathon\content2.txt", "r")
s=f.read()
from py_bing_search import PyBingWebSearch

'''
search_term = "Python Software Foundation"
bing_web = PyBingWebSearch('1jJ4jrq6jGMZl9fWXwVT9DiaIAZjDdNiByM/hdcstfI', search_term, web_only=False) 
first_fifty_result= bing_web.search(limit=6, format='json') #1-50
#second_fifty_result= bing_web.search(limit=50, format='json') #51-100
'''
##s
from correct import *
s=corrections(s)



search_term =s
bing_web = PyBingWebSearch('1jJ4jrq6jGMZl9fWXwVT9DiaIAZjDdNiByM/hdcstfI', search_term, web_only=False) 
x = bing_web.search(limit=6, format='json') 


results=[]
for i in range(len(x)):
    results+=[(x[i].title,x[i].description,x[i].url)]



from py_bing_search import PyBingImageSearch

bing_image = PyBingImageSearch('1jJ4jrq6jGMZl9fWXwVT9DiaIAZjDdNiByM/hdcstfI', s,
                               image_filters='Size:medium+Color:Monochrome') #image_filters is optional

photos = bing_image.search(limit=6, format='json')

images=[]
for i in range(len(photos)):
    images+=[(photos[i].media_url,photos[i].source_url)]



###titles must not be used


def predefined_code():
    return "<!doctype html><html lang='en'>\
		<head>\
			<meta http-equiv='content - type'content='text / html;charset = utf - 8'>\
			<title>Augmented Reality</title>\
			<meta name='viewport'\
    .content = 'width = device - width, initial - scale = 1.0'>\
			<style type='text/css'>\
				.content {\
				width:1200px; margin: 0 auto;}\
    .img-list1 {\
    				float : left; margin-left:20px; \
    				border-radius: 10px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19); width:150px; \
    				padding:15px 0;}\
    .img-list2 {\
    				float : right; margin-left:20px; \
    				border-radius: 10px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19); width:150px; \
    				padding:15px 0;}\
    .message {\
    				margin:30px; \
    				border-radius: 10px; box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19); width:300px; \
    				padding:15px 0;}\
    </style > \
                </head> \
                    <body> <div class='content'>"


'''
         div {
            width: 300px;
            height: 100px;
            background-color: pink;
            border: 1px solid black;
         }
         div#image-list1 {
            -ms-transform: rotate(-0deg);
            -webkit-transform: rotate(-0deg);
            transform: rotate(-0deg);
         }
      </style>

   </head>
   <body>
      <div>
      Tutorials point.com.
      </div>

      <div id="myDiv">
      <a href=image1 ></a>
      </div>
   </body>
</html>
'''

'''
def image_css_code(images):
    s = ''
    for i in range(len(images)):
        s += 'div#image' + str(i) + ' {\
                        \
						\
            -ms-transform: rotate(-0deg); \
            -webkit-transform: rotate(-0deg);	\
            transform: rotate(-0deg);\
            \
         } '

    return s


def text_css_code(results):
    s = ''
    for i in range(len(results)):
        s += 'div#res' + str(i) + ' {\
            -ms-transform: rotate(-0deg); \
            -webkit-transform: rotate(-0deg);	\
            transform: rotate(-0deg);\
         } '
    return s


def intermediate_code():
    return "</style></head>"

'''
def image_code(images):
    s = ''
    for i in range(len(images)):
        if (i / 3 == 0):
            s += '<div class="image-list1">'
            s += '<div id="' + "image" + str(i) + '"><a href="' + images[i][1] + '">\
					<svg width="300" height="200" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\
				 <!-- Created with SVG-edit - http://svg-edit.googlecode.com/ -->\
				 <g>\
				 \
				 <image xlink:href=\
								 "' + images[i][0] + '" \
								id="svg_12"                height="478.00001" width="638" y="-0.00001" x="1"/> \
			   </g>  </svg>  </a> </div>'
        if (i / 3 == 1):
            s += '<div class="image-list2">'
            s += '<div id="' + "image" + str(i) + '"><a href="' + images[i][1] + '">\
					<svg width="300" height="200" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\
				 <!-- Created with SVG-edit - http://svg-edit.googlecode.com/ -->\
				 <g>\
				 \
				 <image xlink:href=\
								 "' + images[i][0] + '" \
								id="svg_12"                height="478.00001" width="638" y="-0.00001" x="1"/> \
			   </g>  </svg>  </a> </div>'

    return s + '</div>'


def text_code(results):  # [1][2]----[0]---
    s = '<div class="image-list1">'
    for i in range(len(results)):
        s += '<p id="res' + str(i) + '">' + results[i][1].encode('ascii', 'ignore') + '\
        <a href=\"' + results[i][2] + '\">More</a></p>'
    return s + '</div>'


def closing_code():
    return "</body></html>"


import os

open_this = open("open_this.html", "w")

open_this.write(predefined_code())

#open_this.write(image_css_code(images))  ##images = list of tuples = (media,source url)
#open_this.write(text_css_code(results))  ##text = list of tuples   = (title,text,url)###don't display title wikipedia

#open_this.write(intermediate_code())  ########

open_this.write(image_code(images))
open_this.write(text_code(results))

open_this.write(closing_code())

open_this.close()

os.system("start open_this.html")
