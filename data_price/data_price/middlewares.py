# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

from scrapy_selenium.middlewares import SeleniumMiddleware
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc
from scrapy_selenium import SeleniumRequest
from scrapy_selenium.middlewares import SeleniumMiddleware
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from scrapy.utils.project import get_project_settings
from w3lib.http import basic_auth_header
import random

proxyPools = open("/Users/vietnguyen/Desktop/Deep learning/predict_bds_project2/my_project/proxies.txt", "r").read().split("\n")


class DataPriceSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class DataPriceDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        proxy = random.choice(proxyPools).split(":")
        httpsProxy = proxy[0]
        portProxy = proxy[1]
        usernameProxy = proxy[2]
        passwordProxy = proxy[3]

        request.meta['proxy'] = "http://" + httpsProxy + ":" + portProxy
        request.headers['Proxy-Authorization'] = basic_auth_header(usernameProxy, passwordProxy) 

        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)

class ProxiedSeleniumMiddleware(SeleniumMiddleware):
    def process_request(self, request, spider):
        if request.meta.get('proxy'):
            # Extract proxy from request metadata
            proxy = request.meta['proxy']
            # Add proxy to chrome options
            chrome_options = Options()
            chrome_options.add_argument(f'--proxy-server={proxy}')
            request.meta['driver_options'] = chrome_options
            
        return super().process_request(request, spider)
    
class UndetectableSeleniumMiddleware(SeleniumMiddleware):
    def __init__(self, driver_name, driver_executable_path, browser_executable_path,
                 driver_arguments, driver_kwargs):
        """Initialize the middleware with undetected Chrome"""
        # Save original parameters
        self.driver_name = driver_name
        self.driver_executable_path = driver_executable_path
        self.browser_executable_path = browser_executable_path
        self.driver_arguments = driver_arguments
        self.driver_kwargs = driver_kwargs
        # We don't create the driver here - it will be created per request
        self.drivers = {}
        
    def get_driver(self, request):
        """Create undetected ChromeDriver on demand"""
        options = uc.ChromeOptions()
        # Add proxy if available
        if request.meta.get('proxy'):
            proxy = request.meta['proxy']
            options.add_argument(f'--proxy-server={proxy}')
        
        # Add any other arguments
        for argument in self.driver_arguments:
            options.add_argument(argument)
        
        driver = uc.Chrome(
            options=options,
            use_subprocess=True,  # Important for undetectability
        )
        return driver
    
class RandomUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent='Scrapy'):
        self.user_agent = user_agent
        settings = get_project_settings()
        self.user_agent_choices = settings.get('USER_AGENT_CHOICES', [])

    def process_request(self, request, spider):
        if self.user_agent_choices:
            user_agent = random.choice(self.user_agent_choices)
            request.headers['User-Agent'] = user_agent
            # Log the user agent (optional)
            spider.logger.debug(f'Using User-Agent: {user_agent}')
