import os
import requests
from urllib.parse import urlparse
import hashlib

# === Ubuntu-inspired Image Fetcher ===
# "I am because we are" -> This program fetches and organizes images with respect.

def fetch_images(urls):
    # Create directory if not exists
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    for url in urls:
        try:
            # Send GET request with a user-agent for respect
            headers = {"User-Agent": "UbuntuFetcher/1.0 (Respectful Client)"}
            response = requests.get(url, headers=headers, timeout=10)

            # Check HTTP response status
            response.raise_for_status()

            # Validate content-type (only allow images)
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print(f"⛔ Skipped: {url} (Not an image)")
                continue

            # Generate safe filename
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)

            if not filename:  # If no filename, create one
                # Use hash of URL to avoid duplicates
                filename = hashlib.md5(url.encode()).hexdigest() + ".jpg"

            filepath = os.path.join(save_dir, filename)

            # Check for duplicates
            if os.path.exists(filepath):
                print(f"⚠️ Skipped duplicate: {filename}")
                continue

            # Save file in binary mode
            with open(filepath, "wb") as f:
                f.write(response.content)

            print(f"✅ Downloaded: {filename}")

        except requests.exceptions.RequestException as e:
            print(f"⚠️ Error fetching {url}: {e}")


if __name__ == "__main__":
    # Prompt user for single or multiple URLs
    user_input = input("Enter image URL(s), separated by commas: ").strip()
    urls = [u.strip() for u in user_input.split(",") if u.strip()]

    if urls:
        fetch_images(urls)
    else:
        print("No URLs provided. Exiting.")
