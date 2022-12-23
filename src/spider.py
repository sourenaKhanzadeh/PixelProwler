import requests
from bs4 import BeautifulSoup

class Spider:
    def __init__(self):
        self.base_url = 'https://www.google.com/search?q='
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        self.queue = []

    def crawl(self, query):
        """Sends a search request to Google and returns the HTML content of the search results page."""
        query = query.replace(' ', '+')
        url = self.base_url + query
        response = requests.get(url, headers=self.headers)
        html = response.text

        return html

    def _extract_links(self, html):
        """Extracts all links from the specified HTML content."""
        soup = BeautifulSoup(html, 'html.parser')
        links = []
        for a in soup.find_all('a'):
            href = a.get('href')
            if href and 'url?q=' in href and 'webcache' not in href:
                links.append(href.split('?q=')[1].split('&sa=')[0])
        return links
