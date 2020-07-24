# coding: utf-8
#python file_resize.py dir_path(foldername) size
import os
import sys
from PIL import Image, ImageDraw, ImageFilter

def resize_square(img, background_color):
    img_width, img_height = img.size
    if img_width == img_height:
        return img
    elif img_width > img_height:
        result = Image.new(img.mode, (img_width, img_width), background_color)
        result.paste(img, (0, (img_width - img_height) // 2))
        return result
    else:
        result = Image.new(img.mode, (img_height, img_height), background_color)
        result.paste(img, ((img_height - img_width) // 2, 0))
        return result
        
def rotate(img, angle):
    result = img.rotate(angle)
    return result


if __name__ == '__main__':
    args = sys.argv
    child_dir = args[1] + "/"
    for file_name in os.listdir(child_dir):
        if file_name.endswith('.jpg') or file_name.endswith('.png'):
            img = Image.open(child_dir + file_name)
            img_width, img_height = img.size
            out = resize_square(img, (0, 0, 0)).resize((int(args[2]), int(args[2])), Image.LANCZOS)
#            out = rotate(img, int(args[2]))
            out.save(child_dir + file_name, quality=95)
