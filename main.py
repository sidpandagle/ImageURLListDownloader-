import requests
import random

def download_imgs(file):
    with open(file, 'r') as url_file:
        data = url_file.read().strip().split('\n') # Read the URLs in the file
    for url in data:
        img = requests.get(url.strip()) # Open the link
        with open(url.split('/')[-1], 'wb') as write_img:
            # Random module to generate a random name for the image
            write_img.write(img.content)
            # Saved the image
    return True

download_imgs('./url-list.txt')