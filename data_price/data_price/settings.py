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



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "data_price (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0',
    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'
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


# Improved proxy loading with better error handling
import os
proxies_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'proxies.txt')

try:
    with open(proxies_path, 'r') as f:
        ROTATING_PROXY_LIST = [line.strip() for line in f if line.strip()]
    print(f"Loaded {len(ROTATING_PROXY_LIST)} proxies from {proxies_path}")
    if not ROTATING_PROXY_LIST:
        print("Warning: Proxy file exists but contains no valid proxies")
except Exception as e:
    print(f"Error loading proxies from {proxies_path}: {e}")
    # Fallback list if needed
    ROTATING_PROXY_LIST = []

# Longer timeout to account for proxies
DOWNLOAD_TIMEOUT = 180

# Additional parameters for better proxy management
ROTATING_PROXY_PAGE_RETRY_TIMES = 5  # Retry failed requests with different proxies
ROTATING_PROXY_BACKOFF_BASE = 300  # Wait time between retries (seconds)
ROTATING_PROXY_BACKOFF_CAP = 3600  # Maximum wait time


# import os
# import random
# from pathlib import Path

# BOT_NAME = "data_price"

# SPIDER_MODULES = ["data_price.spiders"]
# NEWSPIDER_MODULE = "data_price.spiders"

# # Disable robots.txt for maximum scraping capability (use with caution and respect target websites)
# ROBOTSTXT_OBEY = False

# # ------- PROXY CONFIGURATION -------
# # Load and format proxies from file
# def load_proxies():
#     proxies = []
#     proxy_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '../', 'proxies.txt')
    
#     try:
#         with open(proxy_path, 'r') as f:
#             for line in f:
#                 line = line.strip()
#                 if line:
#                     try:
#                         # Parse IP:PORT:USERNAME:PASSWORD format
#                         parts = line.split(':')
#                         if len(parts) == 4:
#                             ip, port, username, password = parts
#                             # Format for Scrapy: http://username:password@ip:port
#                             proxy = f'http://{username}:{password}@{ip}:{port}'
#                             proxies.append(proxy)
#                     except Exception as e:
#                         print(f"Error parsing proxy line: {line}, Error: {e}")
        
#         print(f"Successfully loaded {len(proxies)} proxies")
#         return proxies
#     except Exception as e:
#         print(f"Error loading proxy file: {e}")
#         return []

# ROTATING_PROXY_LIST = load_proxies()

# # Ensure we have proxies
# if not ROTATING_PROXY_LIST:
#     print("WARNING: No proxies loaded! Scraping will proceed without proxies.")

# # ------- OPTIMIZED REQUEST SETTINGS -------
# # Vary download delay to avoid patterns (between 3-7 seconds)
# DOWNLOAD_DELAY = 5
# RANDOMIZE_DOWNLOAD_DELAY = True

# # Concurrency settings - keep low for better proxy rotation
# CONCURRENT_REQUESTS = 2
# CONCURRENT_REQUESTS_PER_DOMAIN = 1
# CONCURRENT_REQUESTS_PER_IP = 1

# # Enable cookies for sites that require session persistence
# COOKIES_ENABLED = True

# # ------- USER AGENT CONFIGURATION -------
# # Rotate user agents to avoid detection
# USER_AGENT_CHOICES = [
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 11.5; rv:90.0) Gecko/20100101 Firefox/90.0',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
# ]

# # ------- SELENIUM CONFIGURATION -------
# SELENIUM_DRIVER_NAME = 'chrome'
# SELENIUM_DRIVER_EXECUTABLE_PATH = None  # Let webdriver-manager handle it
# SELENIUM_DRIVER_ARGUMENTS = [
#     '--no-sandbox',
#     '--disable-dev-shm-usage',
#     '--disable-gpu',
#     '--disable-extensions',
#     '--disable-blink-features=AutomationControlled',  # Hide WebDriver usage
#     '--window-size=1920,1080'
# ]
# SELENIUM_BROWSER_EXECUTABLE_PATH = None

# # ------- MIDDLEWARE CONFIGURATION -------
# # Integrated middleware setup with proper priorities
# DOWNLOADER_MIDDLEWARES = {
#     # Disable default user-agent middleware
#     'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    
#     # Proxy middleware
#     'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
#     'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
    
#     # Custom middlewares
#     'data_price.middlewares.RandomUserAgentMiddleware': 400,  # We'll create this
#     'data_price.middlewares.UndetectableSeleniumMiddleware': 800,
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 600,
#     'data_price.middlewares.DataPriceDownloaderMiddleware': 543,
    
#     # Retry middleware with high priority
#     'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
# }

# # Retry settings for failed requests
# RETRY_ENABLED = True
# RETRY_TIMES = 5  # Try 5 times
# RETRY_HTTP_CODES = [500, 502, 503, 504, 408, 429, 403]  # Common error codes

# # Proxy settings
# ROTATING_PROXY_PAGE_RETRY_TIMES = 5  # Retry with different proxies
# ROTATING_PROXY_CLOSE_SPIDER = False  # Don't close spider if all proxies are exhausted

# # ------- GENERAL SETTINGS -------
# REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
# TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
# FEED_EXPORT_ENCODING = "utf-8"

# # ------- TIMEOUT SETTINGS -------
# DOWNLOAD_TIMEOUT = 180  # 3 minutes timeout