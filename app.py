import os
import requests
import time

# ====== CONFIGURATION ======
PEXELS_API_KEY = "" # Pexels API Key
SEARCH_QUERIES = ["mountains", "sea", "nature", "city"]  # Multiple queries
TOTAL_IMAGES_PER_QUERY = 125  # Number of images per query
IMAGES_PER_PAGE = 80  # Max per request (Pexels limit)
IMAGE_ORIENTATION = "landscape"  # Options: 'landscape', 'portrait', 'square'
IMAGE_SIZE = "large"  # Options: 'small', 'medium', 'large'
IMAGE_COLOR = None  # 'black', 'white', 'red', etc. (Set to None to ignore)
SAVE_FOLDER = "pexels_images"  # Main save folder

os.makedirs(SAVE_FOLDER, exist_ok=True)

headers = {"Authorization": PEXELS_API_KEY}

def download_images_for_query(query):
    query_folder = os.path.join(SAVE_FOLDER, query.replace(" ", "_"))
    os.makedirs(query_folder, exist_ok=True)

    print(f"\n🔹 Downloading up to {TOTAL_IMAGES_PER_QUERY} images for '{query}'...")

    page = 1
    downloaded_count = 0

    while downloaded_count < TOTAL_IMAGES_PER_QUERY:
        remaining_images = TOTAL_IMAGES_PER_QUERY - downloaded_count
        images_to_fetch = min(IMAGES_PER_PAGE, remaining_images)

        pexels_url = f"https://api.pexels.com/v1/search?query={query}&per_page={images_to_fetch}&page={page}&orientation={IMAGE_ORIENTATION}&size={IMAGE_SIZE}"
        if IMAGE_COLOR:
            pexels_url += f"&color={IMAGE_COLOR}"

        response = requests.get(pexels_url, headers=headers)

        if response.status_code == 200:
            images = response.json().get("photos", [])

            if not images:
                print(f"⚠️ No more images found for '{query}'. Stopping download.")
                break

            for img in images:
                downloaded_count += 1
                img_url = img["src"]["original"]  # Get high-quality image
                img_path = os.path.join(query_folder, f"{query}_{downloaded_count}.jpg")

                try:
                    img_data = requests.get(img_url).content
                    with open(img_path, "wb") as file:
                        file.write(img_data)
                    print(f"✅ Downloaded {downloaded_count} for '{query}': {img_path}")
                except Exception as e:
                    print(f"⚠️ Error downloading {img_url}: {e}")

                if downloaded_count >= TOTAL_IMAGES_PER_QUERY:
                    break

            page += 1  # Move to the next page
            time.sleep(1)  # Avoid API rate limits

        else:
            print(f"❌ Error fetching images for '{query}': {response.status_code} {response.text}")
            break

    print(f"🎉 Finished downloading {downloaded_count} images for '{query}'!")

for search_query in SEARCH_QUERIES:
    download_images_for_query(search_query)

print("\n🚀 All downloads complete!")