from PIL import Image
import sys


Image.MAX_IMAGE_PIXELS = None

def upscale_image(input_path, output_path, scale_factor):
    
    with Image.open(input_path) as img:
        
        original_width, original_height = img.size
        
        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)
        
        upscaled_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        upscaled_img.save(output_path)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python upscale_image.py <input_image> <output_image> <scale_factor>")
        sys.exit(1)

    input_image = sys.argv[1]
    output_image = sys.argv[2]
    try:
        scale_factor = float(sys.argv[3])
    except ValueError:
        print("Scale factor must be a number.")
        sys.exit(1)

    if scale_factor <= 1:
        print("Scale factor must be greater than 1 to increase file size.")
        sys.exit(1)

    upscale_image(input_image, output_image, scale_factor)
    print(f"Image upscaled and saved as {output_image}")
