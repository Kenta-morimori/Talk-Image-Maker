import cv2
import requests #URLから画像を持ってくる

def add(f1, f2, out, top, left): #画像合成の関数
    img1 = cv2.imread(f1)
    img2 = cv2.imread(f2)

    img2 =cv2.resize(img2,(600,600)) #サイズ調節

    height, width = img1.shape[:2]
    img2[top:height + top, left:width + left] = img1

    cv2.imwrite(out, img2)

add_url = 'https://user-images.githubusercontent.com/64821676/98765274-19c82580-2421-11eb-8b17-c2e6af55c0ae.jpg' #入力する画像のURL
Temp_url = 'https://user-images.githubusercontent.com/64821676/98764622-893d1580-241f-11eb-9a37-704948ba7d42.jpeg' #テンプレ画像のURL

response = requests.get(add_url)
add_img = response.content
response = requests.get(Temp_url)
Temp_img = response.content

add(Temp_img, add_img, 'new_img.jpg', 30, 60) #合成したい画像、合成の背景にしたい画像、出力先、合成する位置の y 座標、x 座標を指定

print('new_img.jpg') #画像の表示(add()の３つ目の引数)