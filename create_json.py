# coding: utf-8
#python create_json.py dir_path tag_name
import os
import sys
from PIL import Image
import json
import random, string

def randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

def save_json(dir_path, file_name, img, tag):
    if os.path.exists(dir_path):
        create_json(dir_path, file_name, img, tag)
    else:
        os.makedirs(dir_path)
        create_json(dir_path, file_name, img, tag)

def create_json(dir_path, file_name, img, tag):
    img_width, img_height = img.size
    yolo = {
            "asset": {
                "format": str(os.path.splitext(file_name)[1])[1:],
                "id": randomname(32),
                "name": str(file_name),
                "path": "file:" + str(os.path.abspath(child_dir + file_name)),
                "size": {
                    "width": img_width,
                    "height": img_height
                },
                "state": 2,
                "type": 1
            },
            "regions": [
                {
                    "id": randomname(9),
                    "type": "RECTANGLE",
                    "tags": [
                        str(tag)
                    ],
                    "boundingBox": {
                        "height": img_height,
                        "width": img_width,
                        "left": 0,
                        "top": 0
                    },
                    "points": [
                        {
                            "x": 0,
                            "y": 0
                        },
                        {
                            "x": img_width,
                            "y": 0
                        },
                        {
                            "x": img_width,
                            "y": img_height
                        },
                        {
                            "x": 0,
                            "y": img_height
                        }
                    ]
                }
            ],
            "version": "2.2.0"
    }
    with open(os.path.join(dir_path, str(os.path.splitext(file_name)[0]) + ".json"), mode = 'w') as f:
         out = json.dumps(yolo, f, ensure_ascii=False, indent=4)
         f.write(out)

if __name__ == '__main__':
    args = sys.argv
    child_dir = args[1] + "/"
    for file_name in os.listdir(child_dir):
        img = Image.open(child_dir + file_name)
        save_json(child_dir+"json", file_name, img, args[2])
