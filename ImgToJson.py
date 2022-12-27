# JPG to JSON converter.
# It creates a json file with a list of RGB of all pixels of the image.
# It is very slow and the json file is muuuch bigger than the original image.

import os
from PIL import Image
import json

working_directory = os.path.abspath(os.getcwd())
img_directory = os.path.join(working_directory, 'IMG')
json_directory = os.path.join(working_directory, 'JSON')

images = os.listdir('IMG')

i = 0
target_image_path = os.path.join(img_directory, images[i])

target_image = Image.open(target_image_path)
img_width, img_height = target_image.size

json_image = {}

pixels = []

for x in range(img_width):
    for y in range(img_height):
        r, g, b = target_image.getpixel((x, y))
        pixel = {
            'x':x,
            'y':y,
            'R':r,
            'G':g,
            'B':b
            }
        pixels.append(pixel)
        #json_image.update(pixel)
        
json_image.update({'name':images[i], 'height':img_height, 'width':img_width})

output_json_path = os.path.join(json_directory, images[i].split('.')[0] + '.json')

# Serializing json
json_object = json.dumps(json_image, indent=4)
json_object = json.dumps(pixels, indent=4)

with open(output_json_path, 'w') as json_file:
    json_file.write(json_object)

 