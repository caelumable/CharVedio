Skip to content
 
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 @caelumable Sign out
0
0 0 caelumable/CharVedio
 Code  Issues 0  Pull requests 0  Projects 0  Wiki  Insights  Settings
CharVedio/charvedio.py
1c78d87  3 minutes ago
@caelumable caelumable new file
     
153 lines (129 sloc)  4.28 KB
# -*- coding:utf-8 -*-
# coding:utf-8

import os

import cv2
from cv2 import VideoWriter, VideoWriter_fourcc, imread, resize
from PIL import Image, ImageDraw, ImageFont

ascii_char = list(
    "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:oa+>!:+. ")


def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ''
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]



def txt2image(file_name):
    im = Image.open(file_name)
    be_width = im.width
    be_height = im.height
    '''
    #这里要注意，因为使用字符代替像素点，所以字符的大小要尽量和像素点一致，那么就要把图像缩小一下
    #那么缩小以后再用原来大小的画布画画面，相等与把一个像素点放大了，那么就可以用字符代替了,所以这里的参数6，15是经验得到的数据
    
    '''
    width = int(be_width / 6)
    height = int(be_height / 15)
    im = im.resize((width, height), Image.NEAREST)
    txt = ""
    colors = []
    for i in range(height):
        for j in range(width):
            pixel = im.getpixel((j, i))
            # 下面的这个只是担心有的像素会有透明度的参数，所以分开来考虑
    
        #      if (len(pixel) == 4):
        #             txt += get_char(pixel[0], pixel[1], pixel[2], pixel[3])
        #    else:
        #           txt += get_char(pixel[0], pixel[1], pixel[2])
            txt += get_char(pixel[0], pixel[1], pixel[2])
            colors.append((pixel[0], pixel[1], pixel[2]))
        # 因为下面的每一个字符都要对应有颜色，所以如果txt加了一个回车，那么对应颜色也应该加一个，不然会产生不对应的情况，造成inde溢出
        txt += '\n'
        colors.append((255, 255, 255))
    # 建立新的画布
    new_txt = Image.new("RGB", (be_width, be_height), (255, 255, 255))
    # 在新画布上画画
    draw = ImageDraw.Draw(new_txt)
    font = ImageFont.load_default().font
    x = y = 0
    font_w, font_h = font.getsize(txt[1])
    # 留下一些间距
    font_h *= 1.25
    for i in range(len(txt)):
        if (txt[i] == '\n'):
            x += font_h
            y = 0
        # self, xy, text, fill = None, font = None, anchor = None,
            # *args, ** kwargs
        draw.text((y, x), txt[i],  fill=colors[i])
        # dr.text((y, x), txt[i], font=font, fill=colors[i])
        y += font_w
    new_txt.save(file_name)

#把video转变成一系列图片
def videoToIm(videoPath):
    vc=cv2.VideoCapture(videoPath)
    c = 1
    if vc.isOpened(): 
        r,frame=vc.read()
        if not os.path.exists('Cache'):
            os.mkdir('Cache')
        os.chdir('Cache')
    else:
        r=False

    while r:
        cv2.imwrite(str(c)+'.jpg',frame)
        txt2im(str(c)+'.jpg')
        r,frame=vc.read()
        c+=1
    os.chdir('..')

def ImTOVedio():
    cv2=132sadl


'''
txt2image(r'E:\2.jpg')
'''
© 2019 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
Press h to open a hovercard with more details.