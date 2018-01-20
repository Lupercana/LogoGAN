# To run: python3 ..../transform_image.py <path to folder of files to transform> <path to output folder> <desired file extension, EX: '.png'> <desired width and height>

from PIL import Image
import sys
import os
import math
import cairosvg

input_folder = sys.argv[1]
output_folder = sys.argv[2]
output_image_type = sys.argv[3]
output_image_sl = int(sys.argv[4]) # Output image side length, make all output square images for now

onlyfiles = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

count = 0
for im in range(len(onlyfiles)):
    if (count % 100 == 0):
        print(str(count) + ' / ' + str(len(onlyfiles)))
    count += 1

    file_name, file_ext = os.path.splitext(onlyfiles[im])
    img = Image.open(input_folder + onlyfiles[im])

    width, height = img.size
    largest_side = max(width, height)

    #print(width)
    #print(height)
    # Resize if necessary
    new_width = width
    new_height = height
    if (largest_side > output_image_sl):
        scale = output_image_sl / float(largest_side)
        new_width = int(width * scale)
        new_height = int(height * scale) 
        img = img.resize((new_width, new_height), Image.ANTIALIAS)

    # Add whitespace if necessary
    x1 = int(math.floor((output_image_sl - new_width) / 2))
    y1 = int(math.floor((output_image_sl - new_height) / 2))

    #print(img.size)
    enlarged_img = Image.new('RGBA', (output_image_sl, output_image_sl), (255, 255, 255))
    enlarged_img.paste(img, (x1, y1))

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    enlarged_img.save(output_folder + file_name + output_image_type)

