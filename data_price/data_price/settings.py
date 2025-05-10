# Scrapy settings for data_price project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "data_price"

SPIDER_MODULES = ["data_price.spiders"]
NEWSPIDER_MODULE = "data_price.spiders"

import os 
proxies_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'proxies.txt')
# Load proxies from file
try:
    with open(proxies_path, 'r') as f:
        ROTATING_PROXY_LIST = [line.strip() for line in f if line.strip()]
    print(f"Loaded {len(ROTATING_PROXY_LIST)} proxies from {proxies_path}")
except Exception as e:
    print(f"Error loading proxies from {proxies_path}: {e}")
    ROTATING_PROXY_LIST = []


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "data_price (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0',
}
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "data_price.middlewares.DataPriceSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "data_price.middlewares.DataPriceDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "data_price.pipelines.DataPricePipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
# Set base download delay to 7.5 seconds
DOWNLOAD_DELAY = 5

# Enable randomization (will vary between 0.5 and 1.5 times the DOWNLOAD_DELAY)
# This gives a range of approximately 3.75-11.25 seconds
RANDOMIZE_DOWNLOAD_DELAY = True

# Set concurrent requests to 1 to ensure delays work properly
CONCURRENT_REQUESTS = 1

# Add these settings
SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = None  # Let webdriver-manager handle it
SELENIUM_DRIVER_ARGUMENTS = [
    # '--headless',
    '--no-sandbox',
    '--disable-dev-shm-usage',
    '--disable-gpu',
    '--disable-extensions'
]  # Run in headless mode
SELENIUM_BROWSER_EXECUTABLE_PATH = None


# # Rotating proxies settings
# ROTATING_PROXY_LIST = [
#     # Add your proxy list here
#     '38.154.227.167:5868',
#     # You'll need to replace with real proxies
# ]

# Configure middlewares with correct order
DOWNLOADER_MIDDLEWARES = {
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
    'data_price.middlewares.UndetectableSeleniumMiddleware': 800,
    # Comment out the regular selenium middleware
    # 'scrapy_selenium.SeleniumMiddleware': None,
}

# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 600,  
#     'data_price.middlewares.DataPriceDownloaderMiddleware': 543,
# }

# Longer timeout to account for proxies
DOWNLOAD_TIMEOUT = 180
