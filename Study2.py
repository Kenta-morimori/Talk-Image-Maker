# from PIL import Image, ImageDraw, ImageFilter #旧案

# im1 = Image.open('') #入力する画像
# im2 = Image.open('') #テンプレ画像

# back_im = im1.copy()
# back_im.paste(im2, (100, 50)) #(左上のx座標, 左上のy座標)
# back_im.save('data/dst/rocket_pillow_paste_pos.jpg', quality=95)

import cv2
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

def add(f1, f2, out, top, left): #画像合成の関数
    img1 = cv2.imread(f1)
    img2 = cv2.imread(f2)

    img2 =cv2.resize(img2,(600,600)) #サイズ調節

    height, width = img1.shape[:2]
    img2[top:height + top, left:width + left] = img1

    cv2.imwrite(out, img2)



img1 = cv2.imread('') #入力する画像
img2 = cv2.imread('') #テンプレ画像


add('president.jpg', 'park.jpg', 'new.jpg', 30, 60) #合成したい画像、合成の背景にしたい画像、出力先、合成する位置の y 座標、x 座標を指定

print() #画像の表示(add()の３つ目の引数)