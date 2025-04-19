from PIL import Image, ImageDraw, ImageFont
import os

def create_logo():
    """Create a simple logo for the application"""
    # Create a blank image with a white background
    img = Image.new('RGB', (400, 400), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    
    # Draw a green circle
    d.ellipse((50, 50, 350, 350), fill=(76, 175, 80))
    
    # Draw a lighter green circle for the melon pattern
    d.ellipse((75, 75, 325, 325), fill=(129, 199, 132))
    
    # Draw some melon stripes
    for i in range(0, 360, 30):
        x1 = 200 + 125 * (i / 360)
        y1 = 200
        x2 = 200
        y2 = 200 + 125 * (i / 360)
        d.line([(200, 200), (x1, y1)], fill=(76, 175, 80), width=5)
        d.line([(200, 200), (x2, y2)], fill=(76, 175, 80), width=5)
    
    # Save the image
    os.makedirs("app/static", exist_ok=True)
    img.save("app/static/logo.png")
    print("Logo created successfully!")

if __name__ == "__main__":
    create_logo()