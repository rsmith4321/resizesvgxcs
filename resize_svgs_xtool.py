import os
import xml.etree.ElementTree as ET

def resize_svgs_in_current_folder(target_width_in_inches=None, target_height_in_inches=None, dpi=72):
    # Get the current directory
    current_folder = os.getcwd()

    # Process each SVG file in the folder
    for filename in os.listdir(current_folder):
        if filename.endswith(".svg"):
            input_path = os.path.join(current_folder, filename)

            # Parse the SVG file
            tree = ET.parse(input_path)
            root = tree.getroot()

            # Get the original width, height, or viewBox
            width = root.attrib.get("width")
            height = root.attrib.get("height")
            viewBox = root.attrib.get("viewBox")

            if width and height:
                # Convert width and height to float values (assuming they're in pixels)
                original_width = float(width.replace("px", ""))
                original_height = float(height.replace("px", ""))

            elif viewBox:
                # If no width/height but viewBox exists, use it to calculate aspect ratio
                viewBox_values = list(map(float, viewBox.split()))
                original_width = viewBox_values[2]
                original_height = viewBox_values[3]
            else:
                print(f"Skipping {filename}: No valid width/height or viewBox found.")
                continue

            # Calculate new dimensions
            if target_width_in_inches and target_height_in_inches:
                # Convert both to pixels
                new_width = target_width_in_inches * dpi
                new_height = target_height_in_inches * dpi
            elif target_width_in_inches:
                # Calculate height based on aspect ratio
                new_width = target_width_in_inches * dpi
                new_height = (new_width / original_width) * original_height
            elif target_height_in_inches:
                # Calculate width based on aspect ratio
                new_height = target_height_in_inches * dpi
                new_width = (new_height / original_height) * original_width
            else:
                print(f"Skipping {filename}: No width or height specified.")
                continue

            # Update the SVG attributes
            root.attrib["width"] = f"{new_width}px"
            root.attrib["height"] = f"{new_height}px"

            # Save the resized SVG back to the current folder with "_resized" appended to the name
            output_path = os.path.join(current_folder, f"{os.path.splitext(filename)[0]}_resized.svg")
            tree.write(output_path)
            print(f"Resized {filename} to {new_width / dpi:.2f} inches width and {new_height / dpi:.2f} inches height at {dpi} DPI.")

# Prompt the user for the target width and height in inches
try:
    target_width = input("Enter the desired width in inches (leave blank to preserve aspect ratio): ")
    target_height = input("Enter the desired height in inches (leave blank to preserve aspect ratio): ")

    # Convert inputs to floats or None if blank
    target_width = float(target_width) if target_width.strip() else None
    target_height = float(target_height) if target_height.strip() else None

    resize_svgs_in_current_folder(target_width_in_inches=target_width, target_height_in_inches=target_height, dpi=72)
    print("All SVG files have been resized for xTool Creative Space (72 DPI).")
except ValueError:
    print("Invalid input. Please enter numeric values for width and height.")
