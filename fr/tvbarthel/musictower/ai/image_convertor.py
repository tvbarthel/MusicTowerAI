import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
site_packages_path = os.path.join(current_dir, "../../../../lib")

sys.path.append(site_packages_path)

from PIL import Image


def convert_to_black_and_white(in_path, out_path):
    colored_screen_shot = Image.open(in_path)
    grey_scaled_screen_shot = colored_screen_shot.convert('L')
    binarized_screen_shot = grey_scaled_screen_shot.point(lambda x: 255 if x < 254 else 0, '1')
    binarized_screen_shot.save(out_path)


if (len(sys.argv) != 3):
    raise ValueError("Required 2 arguments: the path of the input image and the path of the output image.")

arg_in_path = sys.argv[1]
arg_out_path = sys.argv[2]

print "converting " + arg_in_path + " to " + arg_out_path
convert_to_black_and_white(arg_in_path, arg_out_path)
