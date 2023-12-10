
import sys, os
from PIL import Image  


def crop1px(img):
     """
     상하좌우 딱 1px 크롭한다.
     """
     x,y = img.size

     cropped = img.crop((1,1, x-1, y-1))
     return cropped


def func(path):
     """
     이미지가 들어있는 폴더를 넣어주면 pdf로 안의 이미지를 묶는다. pdf 이름은 폴더명으로 한다. 
     """
     filename = path
     filename += ".pdf"
     images = [Image.open(path + "/" + f) for f in os.listdir(path) ]
     images = [crop1px(x) for x in images]
     images[0].save(filename, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])


if __name__=="__main__":
    
    img_folders = sys.argv[1:]
    print(img_folders)
    for i in img_folders:
         func(i)
