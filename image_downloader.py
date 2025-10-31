import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

def download_images(url, limit, folder="images"):
    """
    Downloads images from a given URL and saves them in a local folder.
    
    Args:
        url (str): The target URL to scrape images from.
        limit (int): Number of images to download.
        folder (str): Destination folder to save images.
    """
    os.makedirs(folder, exist_ok=True)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    count = 0
    for img_tag in soup.find_all("img"):
        img_url = urljoin(url, img_tag.get("src"))
        try:
            img_data = requests.get(img_url).content
            file_path = os.path.join(folder, f"image_{count+1}.jpg")
            with open(file_path, "wb") as f:
                f.write(img_data)
            print(f"✅ Downloaded: {img_url}")
            count += 1
            if count >= limit:
                break
        except Exception as e:
            print(f"❌ Failed to download {img_url}: {e}")

    print(f"\n✅ Finished! Downloaded {count} images to '{folder}' folder.")

# Example:
# download_images("https://example.com", 5)
