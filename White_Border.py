from PIL import Image
import sys

def add_white_border(image_path):
    print("Input image:", image_path)
    img = Image.open(image_path)

    print("Original image size:", img.size)

    # Calculate dimensions for the new image with borders
    width, height = img.size
    max_dim = max(width, height)
    border_size = int(max_dim * 0.05)  # 5% of the maximum dimension

    # Determine the size of the smaller axis after adding borders
    if width < height:
        #new_width = max_dim
        new_height = max_dim + 2 * border_size
        new_width = new_height
    else:
        new_width = max_dim + 2 * border_size
        new_height = new_width
        #new_height = max_dim

    new_size = (new_width, new_height)

    # Create a white background with borders
    whiteness_percentage = 1  # How close to white should the border be (0 = black, 1 = white)
    new_val = int(round(whiteness_percentage*255))
    background = Image.new('RGB', new_size, (new_val, new_val, new_val))

    # Calculate the offset to paste the original image in the center
    offset = ((new_width - width) // 2, (new_height - height) // 2)

    # Paste the original image onto the white background
    background.paste(img, offset)

    print("New image size:", background.size)

    # Save the modified image, overwriting the original
    background.save(image_path)
    print("Output image saved to:", image_path)

if __name__ == "__main__":
    # Check if an image path is provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python add_white_border.py <input_image_path>")
        sys.exit(1)

    image_path = sys.argv[1]

    # Add white border to the image
    add_white_border(image_path)
