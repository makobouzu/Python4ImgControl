#python file_resize.py width height
import os
import sys
from PIL import Image

def down_scale_image(img, scale_width):
    img_width, img_height = img.size
    image = img.resize((scale_width, int(scale_width * img_height / img_width)), Image.LANCZOS)
    return image

def crop_center(img, crop_width, crop_height):
    img_width, img_height = img.size
    area = ((img_width - crop_width)/2, (img_height - crop_height)/2, (img_width + crop_width)/2, (img_height + crop_height)/2)
    return img.crop(area)

if __name__ == '__main__':
    args = sys.argv
    child_dir = '/Volumes/Elements/dataset/StreetView/img/'
    for file_name in os.listdir(child_dir):
        if file_name.endswith('.jpg'):
            img = Image.open(child_dir + file_name)
            out = down_scale_image(img, int(args[1]))
            out = crop_center(img, int(args[1]), int(args[2]))
            out.save(child_dir + file_name, quality=95)
