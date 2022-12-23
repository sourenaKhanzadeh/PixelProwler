import requests
from bs4 import BeautifulSoup

class Spider:
    def __init__(self, base_url):
        self.base_url = base_url
        self.visited = set()

    def crawl(self, url):
        """Crawls the specified URL and returns the HTML content."""
        # Add the URL to the visited set to avoid revisiting
        self.visited.add(url)

        # Send a GET request to the URL and parse the response
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract links from the page and add them to the queue
        links = self._extract_links(soup)
        self._add_to_queue(links)

        # Return the HTML content of the page
        return response.text

    def _extract_links(self, soup):
        """Extracts all links from the specified BeautifulSoup object."""
        links = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and self._is_valid_link(href):
                links.append(href)
        return links

    def _is_valid_link(self, link):
        """Returns true if the specified link is a valid URL to crawl."""
        # Check if the link is an absolute or relative URL
        if link.startswith('http'):
            return True
        elif link.startswith('/'):
            link = self.base_url + link
            return True
        else:
            return False

    def _add_to_queue(self, links):
        """Adds the specified links to the crawl queue if they have not been visited."""
        for link in links:
            if link not in self.visited:
                self.queue.append(link)
