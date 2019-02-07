# -*- coding:utf-8 -*-
# coding:utf-8

import os
import subprocess
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



def txt2im(file_name):
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
        draw.text((y, x), txt[i],  fill=colors[i])
        y += font_w
    new_txt.save(file_name)

#把video转变成一系列图片
def videoToImage(videoPath):
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
    return vc

def Im2vedio(outfilename,fps):
    fourcc=VideoWriter_fourcc('M','J','P','G')
    images = os.listdir('Cache')
    im=Image.open('Cache/'+images[0])
    vw=cv2.VideoWriter(outfilename,fourcc,fps,im.size)

    os.chdir('Cache')

    for image in range(len(images)):
        frame=cv2.imread(str(image+1)+'.jpg')
        vw.write(frame)
    os.chdir("..")

    vw.release()

def remove_dir(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            dirs = os.listdir(path)
            for d in dirs:
                if os.path.isdir(path+'/'+d):
                    remove_dir(path+'/'+d)
                elif os.path.isfile(path+'/'+d):
                    os.remove(path+'/'+d)
            os.rmdir(path)#删除一个空目录
            return
        elif os.path.isfile(path):
            os.remove(path)
        return




if __name__=='__main__':
    INPUT=""#转换视频的地址
    vc = videoToImage(INPUT)
    FPS = vc.get(cv2.CAP_PROP_FPS)#获取帧率
    vc.release()

    #opencv只支持avi格式的视频，所以如果想要转换格式的话建议使用ffmpeg
    Im2vedio(INPUT.split('.')[0]+"1.avi",FPS)

    remove_dir(os.getcwd()+"/Cache")
       

