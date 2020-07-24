#python file_resize.py dir_path size
import os
import sys
from PIL import Image

def down_scale_image(img, scale):
    img_width, img_height = img.size
    if img_width > img_height:
        image = img.resize((scale, int(img_height * scale / img_width)), Image.LANCZOS)
        return image
    elif img_height > img_width:
        image = img.resize((int(img_width * scale / img_height), scale), Image.LANCZOS)
        return image

def crop_center(img, crop):
    img_width, img_height = img.size
    if img_width > img_height:
        area = (0, (img_height - crop)/2, img_width, (img_height + crop)/2)
        return img.crop(area)
    elif img_height > img_width:
        area = ((img_width - crop)/2, 0, (img_height + crop)/2, img_height)
        return img.crop(area)

def rotate(img, angle):
    image = img.rotate(angle)
    return image

if __name__ == '__main__':
    args = sys.argv
    child_dir = args[1] + "/"
    for file_name in os.listdir(child_dir):
        if file_name.endswith('.jpg'):
            img = Image.open(child_dir + file_name)
            out = down_scale_image(img, int(args[2]))
            out = crop_center(img, 0)
            out.save(child_dir + file_name, quality=95)
