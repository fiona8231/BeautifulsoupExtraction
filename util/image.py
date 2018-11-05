import urllib.request


def download(image_url, image_location):
    urllib.request.urlretrieve(image_url, image_location)
