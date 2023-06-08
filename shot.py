import pyscreenshot as ImageGrab
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="name of the screenshot file",
                    type=str)
args = parser.parse_args()

filename = args.filename

def capture_and_crop_screen(crop_positions, output_path):
    # Capture the screen
    screen = ImageGrab.grab()

    # Crop the image to specific positions
    cropped_images = []
    for position in crop_positions:
        cropped_image = screen.crop(position)
        cropped_images.append(cropped_image)

    # Save cropped images as PNG files
    for i, cropped_image in enumerate(cropped_images):
        output_file = f"{output_path}/{filename}.png"
        cropped_image.save(output_file, "PNG")
        print(f"Saved cropped image {i+1} as {output_file}")

# Define the positions to crop (left, upper, right, lower)
crop_positions = [(961, 116, 1918, 1030)]

# Define the output path
output_path = "./output"

# Call the capture_and_crop_screen function
capture_and_crop_screen(crop_positions, output_path)
