import os
import sys
from PIL import Image
from colorama import Fore, Style
from tqdm import tqdm

def merge_images(image_paths, output_filename):
    images = [Image.open(img_path) for img_path in image_paths]
    widths, heights = zip(*(i.size for i in images))

    total_width = max(widths)
    total_height = sum(heights)

    new_image = Image.new('RGB', (total_width, total_height))

    y_offset = 0
    for img in images:
        new_image.paste(img, (0, y_offset))
        y_offset += img.height

    new_image.save(output_filename)

def main():
    if len(sys.argv) < 2:
        print("Usage: \merge_jpgs.exe input_folder optional:[batch_size]")
        return

    input_folder = sys.argv[1]
    batch_size = int(sys.argv[2]) if len(sys.argv) > 2 else 40
    
    output_folder_name = os.path.basename(input_folder) + "_merged"
    output_folder = os.path.join(os.path.dirname(input_folder), output_folder_name)
    
    jpg_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.jpg')]
    jpg_files.sort()

    os.makedirs(output_folder, exist_ok=True)
    
    all_merged = False

    for i in tqdm(range(0, len(jpg_files), batch_size), unit="batch", ncols=100):
        batch = jpg_files[i:i + batch_size]
        merged_filename = f"merged_{i // batch_size + 1}.jpg"
        output_path = os.path.join(output_folder, merged_filename)

        image_paths = [os.path.join(input_folder, img) for img in batch]
        merge_images(image_paths, output_path)
        
        if i + batch_size >= len(jpg_files):
            all_merged = True

    if all_merged:
        print(Fore.GREEN + "All merging completed!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
