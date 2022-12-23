from .spider import Spider
from .image_search import ImageSearch

def search(prompt, num_results=10):
    """Searches the web for images based on the specified prompt and returns a list of image URLs."""
    image_search = ImageSearch()
    image_urls = image_search.search(prompt, num_results)
    return image_urls