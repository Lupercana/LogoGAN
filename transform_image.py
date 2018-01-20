# To run: python3 ..../transform_image.py <path to folder of files to transform> <path to output folder> <desired file extension, EX: '.png'> <desired width and height>

from os import listdir
from os.path import isfile, join, split
import Image

input_folder = sys.argv[1]
output_folder = sys.argv[2]
output_image_type = sys.argv[3]
image_height = sys.argv[4] # For now, make image width same as image height

onlyfiles = [f for f in listdir(input_folder) if isfile(join(input_folder, f))]

for im in range(len(onlyfiles)):

	image = Image.open(onlyfiles[i])
	head, tail = os.path.split(image)
	file_name = os.path.splitext(tail)[0]

	
	
	im.save(head + file_name + output_image_type)

