import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['duckduckgo.com']
    start_urls = ['https://duckduckgo.com/?q=puppies&t=h_&iar=images&iax=images&ia=images']
    saved_images = []

    def parse(self, response):
        # Extract the image URLs from the search results page
        image_urls = response.css('div.tile--img img::attr(src)').getall()

        # Download each image and save it to the current directory
        for url in image_urls:
            yield scrapy.Request(url, callback=self.save_image)

    def save_image(self, response):
        file_name = response.url.split('/')[-1]
        with open(file_name, 'wb') as f:
            f.write(response.body)
        self.saved_images.append(file_name)
        yield {'saved_images': self.saved_images}

