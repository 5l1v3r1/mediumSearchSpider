import scrapy

class StoriesSpider(scrapy.Spider):
    name = "stories"

    def __init__(self, searchString=None, *args, **kwargs):
        super(StoriesSpider, self).__init__(*args, **kwargs)
        #self.start_urls = ['http://www.example.com/categories/%s' % category]
        self.start_urls = ['https://medium.com/search?q=%s' % searchString]

# For All Stories
    def parse(self, response):
        i=1
        for index, story in enumerate(response.css('div.postArticle'), start=1):
            yield {
                'nameOfAuthor': story.xpath(f'/html/body/div[1]/div[2]/div/div[3]/div[2]/div[2]/div[1]/div/div/div[{index}]/div/div[1]/div/div/div[2]/a/text()').extract(),
                'linkOfAuthorProfile': story.xpath('/html/body/div[1]/div[2]/div/div[3]/div[2]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/div[2]/a/@href').extract_first(),
                'article': story.css('div.postArticle-content section div.section-content div h3::text').extract_first(),
                'articleLink': story.css('div.postArticle-readMore a::attr(href)').extract_first(),
                'postingTime': story.xpath(f'/html/body/div[1]/div[2]/div/div[3]/div[2]/div[2]/div[1]/div/div/div[{index}]/div/div[1]/div/div/div[2]/div/a/time/text()').extract_first(),
                'recommendation': story.xpath(f'/html/body/div[1]/div[2]/div/div[3]/div[2]/div[2]/div[1]/div/div/div[{index}]/div/div[4]/div[1]/div/span/button/text()').extract_first(),
                }
