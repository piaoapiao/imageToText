# -*-encoding:utf-8-*-
import pytesseract
from PIL import Image
 
def main():
	image = Image.open("123.png")
	#image.show() #打开图片1.jpg
	text = pytesseract.image_to_string(image,lang='chi_sim') #使用简体中文解析图片
	#print(text)
	with open("output.txt", "w") as f: #将识别出来的文字存到本地
		print(text)
		f.write(str(text))
 
if __name__ == '__main__':
    main()