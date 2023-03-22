#!/usr/bin/python3

import requests
import imghdr


def fetch_image(url):
  # Fetch the image from the URL
  response = requests.get(url)

  # Identify the file type of the image
  image_type = imghdr.what(None, response.content)

  # Determine the appropriate file extension for the image type
  extension = '.' + image_type if image_type else ''
  return (extension, response.content)

if __name__ == "__main__":
  url = 'https://s3.amazonaws.com/eit-planttoolbox-prod/media/images/Betula_alleghaniensis_El_Grafo_ccbysa30.jpg'  # Replace with the URL of the image you want to download
  (extension, content) = fetch_image(url)
  # Save the image to a file with the appropriate file extension
  with open(f'image{extension}', 'wb') as file:
    file.write(content)

  print('Image saved successfully!')
