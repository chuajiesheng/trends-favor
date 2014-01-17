from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log
from testspiders.spiders.followall import FollowAllSpider

spider = FollowAllSpider(domain='scrapinghub.com')
crawler = Crawler(Settings())
crawler.configure()
crawler.crawl(spider)
crawler.start()
log.start()
log.msg('Running reactor...')
reactor.run() # the script will block here
log.msg('Reactor stopped.')
