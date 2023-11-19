#导入scrapy以及自定义库items中的Item类的DdbookItem
import scrapy
from ..items import DdbookItem

#定义爬虫类Ddspider
class DdSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ["dangdang.com"]
    start_urls = ["http://search.dangdang.com/?key=%BC%C6%CB%E3%BB%FA%C0%E0"]
    #定义解析response对象的方法
    def parse(self, response,*args, **kwargs):
        books = response.xpath('//ul[@class="bigimg"]/li')

        #对提取到的所有图书信息进行遍历，提取每一本书的相关信息
        for book in books:
            item = DdbookItem()
            item['name'] = book.xpath('./a[@class="pic"]/@title').extract()
            item['introduction'] = book.xpath('./p[@class="detail"]/text()').extract() #if len(book.xpath('./p[@class="detail"]/text()')) > 0 else '无介绍信息'
            item['author'] = book.xpath('./p[@class="search_book_author"]/span/a/@title').extract() #if len(book.xpath('./p[@class="search_book_author"]/span/a/@title')) > 0 else '无作者信息'
            item['price'] = book.xpath('./p[@class="price"]/span[@class="search_now_price"]/text()').extract()
            item['press'] = book.xpath('./p[@class="search_book_author"]/span[position()=3]/a/@title').extract() #if len(book.xpath('./p[@class="search_book_author"]/span[position()=3]/a/@title')) > 0 else '无出版社信息'
            item['time'] = book.xpath('./p[@class="search_book_author"]/span[position()=2]/text()').extract() #if len(book.xpath('./p[@class="search_book_author"]/span[position()=2]/text()')) > 0 else '无出版时间'
            item['comment_num'] = book.xpath('./p[4]/a[@class="search_comment_num"]/text()').extract() #if len(book.xpath('./p[4]/a[@class="search_comment_num"]/text()').extract) > 0 else '无评论'

            #将提取到的数据提交给pipelines进行保存输出
            yield item

        pageNum = 10
        for page in range(2,pageNum):
            page = 'http://search.dangdang.com/?key=%BC%C6%CB%E3%BB%FA%C0%E0&page_index={}'.format(page)
            yield scrapy.Request(page, callback=self.parse)

