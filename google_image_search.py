#!/usr/bin/python3
import requests

def search_images(query):
    api_key = "<REPLACE WITH YOUR API-KEY>"
    cx = "<REPLACE WITH YOUR CX>"
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "cx": cx,
        "imgSize": "large",
        "imgType": "photo",
        "num": 5,
        "searchType": "image",
        "key": api_key
    }
    response = requests.get(search_url, params=params)
    image_links = []
    if response.status_code == 200:
        try:
            results = response.json()["items"]
            for i, result in enumerate(results):
                #print(f"Image {i + 1}: {result['link']}")
                image_links.append(result['link'])
        except Exception as e:
            print("Exception: ", e)
            print(f'response code: {response.status_code}')
            print(f'response json: "{response.json()}"')
            quit()
    else:
        print(f"Request failed with status code {response.status_code}")

    return (image_links, response.status_code)

if __name__ == "__main__":
    search_term = input("Enter a search term: ")
    (image_links, response_code) = search_images(search_term)
    for i, image_link in enumerate(image_links):
        print(f"Image {i + 1}: {image_link}")
