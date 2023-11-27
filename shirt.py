import sys
import os
from PIL import Image, ImageOps

def main():
    # Argument handling
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py path/to/input_image.png path/to/output_image.png")

    type_input = os.path.splitext(sys.argv[1])
    type_output = os.path.splitext(sys.argv[2])
    if type_input[1] not in (".jpg", ".jpeg", ".png"):
        print(sys.argv[1])
        sys.exit("Input must be jpg, jpeg or png")
    elif type_input[1] != type_output[1]:
        sys.exit("Input and output must be same type")

    # Open images, paste shirt over input image and save
    try:
        with Image.open(sys.argv[1]) as image:
            with Image.open("shirt.png") as shirt:
                image_resized = ImageOps.fit(image, shirt.size)
                image_resized.paste(shirt, mask=shirt)
                image_resized.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input image not found")

if __name__ == "__main__":
    main()