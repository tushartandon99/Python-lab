from PIL import Image

def apply_grayscale(image_path, output_path):
    """Converts image to grayscale by averaging RGB channels."""
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            # Standard luminance formula
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            pixels[x, y] = (gray, gray, gray)
            
    img.save(output_path)
    print(f"Grayscale image saved to {output_path}")

def apply_threshold(image_path, output_path, threshold=128):
    """Applies a black and white threshold to the image."""
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = pixels[x, y]
            gray = int(0.299 * r + 0.587 * g + 0.114 * b)
            # Thresholding logic
            val = 255 if gray >= threshold else 0
            pixels[x, y] = (val, val, val)
            
    img.save(output_path)
    print(f"Threshold (B&W) image saved to {output_path}")

def apply_simple_blur(image_path, output_path):
    """Applies a simple 3x3 spatial box blur using pixel grids."""
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    new_img = Image.new("RGB", img.size)
    new_pixels = new_img.load()
    
    for x in range(1, img.width - 1):
        for y in range(1, img.height - 1):
            r_sum = g_sum = b_sum = 0
            # 3x3 spatial grid iteration
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    r, g, b = pixels[x + dx, y + dy]
                    r_sum += r; g_sum += g; b_sum += b
            
            # Average the colors
            new_pixels[x, y] = (r_sum // 9, g_sum // 9, b_sum // 9)
            
    new_img.save(output_path)
    print(f"Blurred image saved to {output_path}")

if __name__ == "__main__":
    # Note: Requires 'pip install Pillow'
    # sample.jpg must exist in the same directory for this to run
    input_file = "sample.jpg"
    
    try:
        apply_grayscale(input_file, "grayscale_out.jpg")
        apply_threshold(input_file, "threshold_out.jpg", threshold=128)
        apply_simple_blur(input_file, "blur_out.jpg")
    except FileNotFoundError:
        print(f"Error: '{input_file}' not found. Please provide a valid image.")