# Pexels Bulk Image Downloader

This Python script downloads high-quality images in bulk from the Pexels API based on specified search queries. It allows you to download images in different orientations, sizes, and colors, and organizes them into separate folders for each query.

## Features
- Download multiple images per search query.
- Filter images by orientation (landscape, portrait, square).
- Select image size (small, medium, large).
- Optionally filter by image color.
- Saves images in a structured folder based on the query.

## Requirements
- Python 3.x
- `requests` library

## Installation

1. **Install Python:** Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Dependencies:** Install the required Python libraries using pip.

    ```bash
    pip install requests
    ```

3. **Get Pexels API Key:** You need an API key from Pexels to use their API. You can sign up and get the key from [Pexels API](https://www.pexels.com/api/).

## Configuration

1. Set the `PEXELS_API_KEY` variable with your Pexels API key.

2. You can modify the following variables:
    - `SEARCH_QUERIES`: List of search terms for which you want to download images.
    - `TOTAL_IMAGES_PER_QUERY`: Total number of images to download for each search query.
    - `IMAGES_PER_PAGE`: Number of images per request (up to 80 images per request).
    - `IMAGE_ORIENTATION`: Choose between `'landscape'`, `'portrait'`, or `'square'`.
    - `IMAGE_SIZE`: Choose between `'small'`, `'medium'`, or `'large'`.
    - `IMAGE_COLOR`: Optionally filter images by color (e.g., `'black'`, `'white'`, etc.). Leave `None` to ignore color filter.
    - `SAVE_FOLDER`: Name of the folder where images will be saved.

## Usage

Once you've configured the settings, you can run the script:

```bash
python app.py
```

The script will download images from Pexels for each search query and save them into respective folders under the main `pexels_images` folder.

## Example
If you set `SEARCH_QUERIES` to `["mountains", "nature"]`, the script will download images for "mountains" and "nature" and save them in the `pexels_images` directory like this:

```
pexels_images/
    mountains/
        mountains_1.jpg
        mountains_2.jpg
        ...
    nature/
        nature_1.jpg
        nature_2.jpg
        ...
```

## Notes
- The script will download up to 125 images per query (based on the `TOTAL_IMAGES_PER_QUERY` setting).
- If no more images are available for a query, the download for that query will stop.
- API rate limits are handled by adding a `sleep` between requests to avoid hitting the API limits.

## License
This script is free to use under the MIT License.