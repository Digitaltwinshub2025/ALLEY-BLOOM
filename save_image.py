"""
Quick script to help save the alley wall image.
Just drag and drop the image file onto this script or run it and paste the image path.
"""

import shutil
import os

# Create the images directory if it doesn't exist
images_dir = os.path.join('static', 'images')
os.makedirs(images_dir, exist_ok=True)

print("=" * 50)
print("ALLEY BLOOM - Image Setup")
print("=" * 50)
print("\nPlease save your alley wall image as:")
print(f"\n  {os.path.abspath(os.path.join(images_dir, 'alley-wall.jpg'))}")
print("\nOr drag the image file here and press Enter:")

try:
    image_path = input().strip().strip('"')
    
    if os.path.exists(image_path):
        destination = os.path.join(images_dir, 'alley-wall.jpg')
        shutil.copy(image_path, destination)
        print(f"\n✅ Image saved successfully!")
        print(f"   Location: {os.path.abspath(destination)}")
        print("\n🌸 Now refresh your browser at http://localhost:5000")
    else:
        print(f"\n❌ File not found: {image_path}")
        print("\nManually save the image to:")
        print(f"   {os.path.abspath(os.path.join(images_dir, 'alley-wall.jpg'))}")
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nManually save the image to:")
    print(f"   {os.path.abspath(os.path.join(images_dir, 'alley-wall.jpg'))}")

input("\nPress Enter to close...")
