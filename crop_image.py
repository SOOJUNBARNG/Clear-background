from PIL import Image, ImageChops

def autocrop_image(input_path, output_path, padding=20):
    # Open the image
    img = Image.open(input_path)
    
    # 1. Detect background color (assumes top-left pixel is background)
    bg_color = img.getpixel((0, 0))
    bg = Image.new(img.mode, img.size, bg_color)
    
    # 2. Find the difference between the image and the solid background
    diff = ImageChops.difference(img, bg)
    
    # 3. Convert to grayscale and threshold to find the subject area
    mask = diff.convert('L').point(lambda x: 255 if x > 20 else 0)
    
    # 4. Get the bounding box of the subject
    bbox = mask.getbbox()
    
    if bbox:
        # 5. Add a bit of padding so it's not too tight
        left, upper, right, lower = bbox
        left = max(0, left - padding)
        upper = max(0, upper - padding)
        right = min(img.width, right + padding)
        lower = min(img.height, lower + padding)
        
        # 6. Crop and save
        cropped_img = img.crop((left, upper, right, lower))
        cropped_img.save(output_path, quality=95)
        print(f"Success! Image cropped to {cropped_img.size}")
    else:
        print("Could not find a subject to crop.")

# Usage
autocrop_image("logo_output.png", "job_cropped.png")