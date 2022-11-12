from proxyChecker.proxyCheck_process import ProxyController


class ProxyController(ProxyController):
    def __init__(self):
        super().__init__()
                
    def proxyControl(self, proxies, url="https://www.google.com", timeout=(3.05,27),max_redirects=(False,300), details=True):
        """You should send the proxy list you want to check.\n
        proxies  : Proxies parameter must be list or str. (List or String)\n
        url     : Give url to check proxy. (https-http)\n
        timeout : Set a waiting time to connect. Default timeout = (3.05,27) >> (connect,read)\n
        max_redirects : Determines whether redirects are used. Default max_redirects = (False,300) >> (use,value)\n
        details : Information message about whether the proxy is working or not. (True or False)\n
        User Agent : You can find it by typing my user agent into Google.\n
        Default User Agent : Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36"""
        return super().proxyControl(proxies, url, timeout, max_redirects, details)
    
    def getDefaultUseragent(self, useragent="windows"):
        """Default Useragent Values = Windows - linux - macOs - Android - Iphone - Ipad - Ipod\n
            Random UserAgent = Call the randomUserAgent() method for the random user agent."""
        return super().getDefaultUseragent(useragent)
    
    def randomUserAgent(self):
        """
        randomUserAgent = Returns a random useragent when the method is called.\n
        """
        return super().randomUserAgent()