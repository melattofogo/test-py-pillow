import pyscreenshot as ImageGrab
import argparse
import os

def capture_and_crop_screen(crop_positions, output_path, filename, output_format):
    # Capture the screen
    screen = ImageGrab.grab()

    # Crop the image to specific positions
    cropped_images = []
    for position in crop_positions:
        cropped_image = screen.crop(position)
        cropped_images.append(cropped_image)

    # Check for existing files with the same name in the output path
    existing_files = os.listdir(output_path)
    existing_files = [f for f in existing_files if f.startswith(f"{filename}-")]
    index = 0
    while True:
        # Generate a unique filename for each cropped image
        index_str = f"{index:03d}"
        cropped_filename = f"{filename}-{index_str}.{output_format}"
        output_file = os.path.join(output_path, cropped_filename)

        # Save the cropped image if no existing file with the same name
        if cropped_filename not in existing_files:
            cropped_images[index % len(cropped_images)].save(output_file, output_format)
            print(f"Saved cropped image {index + 1} as {output_file}")
            break

        index += 1

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="name of the screenshot file", type=str)
    parser.add_argument("--output-format", help="output format of the cropped images", type=str, default="png")
    parser.add_argument("--output-path", help="output path for saving the screenshot files", type=str, default="./output")
    args = parser.parse_args()

    filename = args.filename
    output_format = args.output_format
    output_path = args.output_path

    # Define the positions to crop (left, upper, right, lower)
    crop_positions = [(961, 116, 1918, 1030)]

    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    # Call the capture_and_crop_screen function
    capture_and_crop_screen(crop_positions, output_path, filename, output_format)

if __name__ == '__main__':
    main()
