from selenium import webdriver

PROXY = '198.50.163.192:3129'
webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",

}
with webdriver.Chrome('/Users/22czarnecki_j/Desktop/chromedriver') as driver:
    driver.get("http://google.com")
    print("Connected with",PROXY)