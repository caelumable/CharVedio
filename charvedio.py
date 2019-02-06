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


    '''
def txt2image(file_name):
    im = Image.open(file_name).convert('RGB')
    # gif��ֺ��ͼ����Ҫת�������򱨴�����gif�ָ�󱣴����������ɫ
    raw_width = im.width
    raw_height = im.height
    width = int(raw_width / 6)
    height = int(raw_height / 15)
    im = im.resize((width, height), Image.NEAREST)

    txt = ""
    colors = []
    for i in range(height):
        for j in range(width):
            pixel = im.getpixel((j, i))
            colors.append((pixel[0], pixel[1], pixel[2]))
            if (len(pixel) == 4):
                txt += get_char(pixel[0], pixel[1], pixel[2], pixel[3])
            else:
                txt += get_char(pixel[0], pixel[1], pixel[2])
        txt += '\n'
        colors.append((255, 255, 255))

    im_txt = Image.new("RGB", (raw_width, raw_height), (255, 255, 255))
    dr = ImageDraw.Draw(im_txt)
    # font = ImageFont.truetype(os.path.join("fonts","���ǿ����.ttf"),18)
    font = ImageFont.load_default().font
    x = y = 0
    # ��ȡ����Ŀ��
    font_w, font_h = font.getsize(txt[1])
    font_h *= 1.37  # ���������
    # ImageDrawΪÿ��ascii�������ɫ
    for i in range(len(txt)):
        if (txt[i] == '\n'):
            x += font_h
            y = -font_w
           # self, xy, text, fill = None, font = None, anchor = None,
            # *args, ** kwargs
        dr.text((y, x), txt[i],  fill=colors[i])
        # dr.text((y, x), txt[i], font=font, fill=colors[i])
        y += font_w

    name = file_name
    # print(name + ' changed')
    im_txt.save(r'E:\3.jpg')
    '''

    '''
def txt2im(file_name):
    im = Image.open(file_name)
    be_width = im.width
    be_height = im.height
    '''
    #����Ҫע�⣬��Ϊʹ���ַ��������ص㣬�����ַ��Ĵ�СҪ���������ص�һ�£���ô��Ҫ��ͼ����Сһ��
    #��ô��С�Ժ�����ԭ����С�Ļ��������棬������һ�����ص�Ŵ��ˣ���ô�Ϳ������ַ�������,��������Ĳ���6��15�Ǿ���õ�������
    
    '''
    width = int(be_width / 6)
    height = int(be_height / 15)
    im = im.resize((width, height), Image.NEAREST)
    txt = ""
    colors = []



    for i in range(height):
        for j in range(width):
            pixel = im.getpixel((j, i))
            # ��������ֻ�ǵ����е����ػ���͸���ȵĲ��������Էֿ�������
    '''
        #      if (len(pixel) == 4):
        #             txt += get_char(pixel[0], pixel[1], pixel[2], pixel[3])
        #    else:
        #           txt += get_char(pixel[0], pixel[1], pixel[2])
    '''
            txt += get_char(pixel[0], pixel[1], pixel[2])
            colors.append((pixel[0], pixel[1], pixel[2]))
        # ��Ϊ�����ÿһ���ַ���Ҫ��Ӧ����ɫ���������txt����һ���س�����ô��Ӧ��ɫҲӦ�ü�һ������Ȼ���������Ӧ����������inde���
        txt += '\n'
        colors.append((255, 255, 255))

    # �����µĻ���
    new_txt = Image.new("RGB", (be_width, be_height), (255, 255, 255))
    # ���»����ϻ���
    draw = ImageDraw.Draw(new_txt)
    font = ImageFont.load_default().font
    x = y = 0
    font_w, font_h = font.getsize(txt[1])
    # ����һЩ���
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
    '''

#��videoת���һϵ��ͼƬ
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
