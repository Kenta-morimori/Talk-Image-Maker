import cv2
import requests #URLから画像を持ってくる
from email.mime import image

# def add(f1, f2, out, top, left): #画像合成の関数
#     img1 = cv2.imread(f1)
#     img2 = cv2.imread(f2)

#     img2 =cv2.resize(img2,(600,600)) #サイズ調節

#     height, width = img1.shape[:2]
#     img2[top:height + top, left:width + left] = img1

#     cv2.imwrite(out, img2)

mat_url = 'https://user-images.githubusercontent.com/64821676/98765274-19c82580-2421-11eb-8b17-c2e6af55c0ae.jpg' #入力する画像のURL
Temp_url = 'https://user-images.githubusercontent.com/64821676/98764622-893d1580-241f-11eb-9a37-704948ba7d42.jpeg' #テンプレ画像のURL

mat_img = cv2.imread(mat_url)
Temp_img = cv2.imread(Temp_url)

cv2.imread(mat_url, mat_img)
cv2.imread(Temp_url, Temp_img)
cv2.waitKey(0)
cv2.destroyAllWindows()