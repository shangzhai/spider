# -*- coding:utf-8 -*-
import urllib2

from spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):

    def __init__(self):
        self.urls=url_manager.UrlManager()
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count=1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url=self.urls.get_new_url()

                new_url=urllib2.unquote(new_url.encode('utf-8'))

                print 'craw %d : %s'%(count,new_url)
                html_content=self.downloader.download(new_url)
                new_urls,new_data=self.parser.parse(new_url,html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collectdata(new_data)


                if count==100:
                    break

                count=count+1
            except:
                print 'craw fails'

        self.outputer.output_html()


if __name__=='__main__':
    root_url='http://baike.baidu.com/item/Python'
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)