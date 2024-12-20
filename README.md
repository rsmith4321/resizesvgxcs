# SVG Batch Resizer for xTool Creative Space

This Python script batch resizes all SVG files in the folder where the script is located. It allows you to specify a desired width and/or height in inches, preserving the aspect ratio if one dimension is left blank. The script is specifically designed for compatibility with **xTool Creative Space**, using a **72 DPI** resolution.

## Features

- Batch processes all SVG files in the same folder as the script.
- Allows you to specify width, height, or both in inches.
- Automatically preserves the aspect ratio if only one dimension is provided.
- Saves resized SVG files with `_resized` appended to their filenames.
- Uses **72 DPI** for perfect size compatibility with xTool Creative Space.

## Requirements

- Python 3.x installed on your system.

## Installation

1. Clone or download this repository.
2. Place the script (`resize_svgs_xtool.py`) in the folder containing the SVG files you want to resize.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the folder containing the script and your SVG files.
3. Run the script with the following command:

   ```bash
   python resize_svgs_xtool.py
   ```

4. Follow the prompts:
   - **Enter the desired width in inches** (leave blank to preserve aspect ratio).
   - **Enter the desired height in inches** (leave blank to preserve aspect ratio).

5. The script will resize all SVG files in the folder and save the resized versions with `_resized` appended to their filenames.

### Example Input

- Enter `1.5` for width and leave height blank:
  - Resizes the width to **1.5 inches** and adjusts the height to maintain the aspect ratio.
- Enter both width (`2.0`) and height (`1.0`):
  - Resizes the SVG to **2 inches wide** and **1 inch tall**, ignoring the original aspect ratio.

## Output

- Resized SVG files are saved in the same folder with filenames like:
  ```
  original_filename_resized.svg
  ```

## Notes

- The script calculates dimensions based on **72 DPI**, which is required for proper size rendering in **xTool Creative Space**.
- If no valid dimensions are specified, the file will be skipped.

## Troubleshooting

- Ensure Python 3.x is installed on your system.
- If you encounter a `ValueError`, ensure you enter valid numeric values for width and height.

## License

This project is open-source and available under the [MIT License](LICENSE).
