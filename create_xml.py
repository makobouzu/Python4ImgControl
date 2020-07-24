# coding: utf-8
#python create_xml.py dir_path tag_name
import os
import sys
from PIL import Image
import xml.etree.ElementTree as ET

def randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

def save_xml(dir_path, file_name, img, tag):
    if os.path.exists(dir_path):
        create_xml(dir_path, file_name, img, tag)
    else:
        os.makedirs(dir_path)
        create_xml(dir_path, file_name, img, tag)

def create_xml(dir_path, file_name, img, tag):
    img_width, img_height = img.size

    #xmlの形式
    annotation     = ET.Element("annotation")
    folder         = ET.SubElement(annotation, "folder")
    folder.text    = str(dir_path)
    filename       = ET.SubElement(annotation, "filename")
    filename.text  = str(os.path.splitext(file_name)[0])
    path           = ET.SubElement(annotation, "path")
    path.text      = str("file:" + str(os.path.abspath(child_dir + file_name)))
    source         = ET.SubElement(annotation, "source")
    database       = ET.SubElement(source, "database")
    database.text  = "Unknown"
    size           = ET.SubElement(annotation, "size")
    width          = ET.SubElement(size, "width")
    width.text     = str(img_width)
    height         = ET.SubElement(size, "height")
    height.text    = str(img_height)
    depth          = ET.SubElement(size, "depth")
    depth.text     = "3"
    segmented      = ET.SubElement(annotation, "segmented")
    segmented.text = "0"
    object         = ET.SubElement(annotation, "object")
    name           = ET.SubElement(object, "name")
    name.text      = str(tag)
    pose           = ET.SubElement(object, "pose")
    pose.text      = "Unspecified"
    truncated      = ET.SubElement(object, "truncated")
    truncated.text = "0"
    difficult      = ET.SubElement(object, "difficult")
    difficult.text = "0"
    bndbox         = ET.SubElement(object, "bndbox")
    xmin           = ET.SubElement(object, "xmin")
    xmin.text      = "0"
    ymin           = ET.SubElement(object, "ymin")
    ymin.text      = "0"
    xmax           = ET.SubElement(object, "xmax")
    xmax.text      = str(img_width)
    ymax           = ET.SubElement(object, "ymax")
    ymax.text      = str(img_height)

    with open(os.path.join(dir_path, str(os.path.splitext(file_name)[0]) + ".xml"), mode = 'w') as f:
         out = ET.dump(annotation)
         f.write(out)  #注意

if __name__ == '__main__':
    args = sys.argv
    child_dir = args[1] + "/"
    for file_name in os.listdir(child_dir):
        img = Image.open(child_dir + file_name)
        save_xml(child_dir+"xml", file_name, img, args[2])
