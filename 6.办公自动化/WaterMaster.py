# 使用Python 去除图片水印
from os.path import splitext
from itertools import product
from PIL import Image
fn = '水印2.png'
im = Image.open(fn)
width,height = im.size
for pos in product(range(width),range(height)):
    if sum(im.getpixel(pos)[:3])>564 :
        im.putpixel(pos,(255,255,255))
im.save('无'.join(splitext(fn)))