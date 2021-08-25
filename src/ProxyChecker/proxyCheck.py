import requests,time,random
from syscolors.sysColors import SystemColors
from proxyChecker.userAgentData import *

clr = SystemColors()
reset = clr.reset

class ProxyController:
    def __init__(self):
        self.__proxysSuccess = []
        self.userAgent = self.getDefaultUseragent()

    def proxyControl(self,proxies,url="https://www.google.com",timeout=(3.05,27),details=True):
        """You should send the proxy list you want to check.\n
        proxies  : Proxies parameter must be list or str. (List or String)\n
        url     : Give url to check proxy. (https-http)\n
        timeout : Set a waiting time to connect. Default timeout = (3.05,27) >> (connect,read)\n
        details : Information message about whether the proxy is working or not. (True or False)\n
        User Agent : You can find it by typing my user agent into Google.\n
        Default User Agent : Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36"""
        try:
            self.__exceptions(proxies,details,url,timeout)
        except Exception as err :
            return print("Error :: > "+str(err))
        URL = url
        TIMEOUT = timeout
        session = requests.Session()
        session.headers['User-Agent'] = self.userAgent
        session.max_redirects = 300
        finishedMsg = "Proxy check completed."

        if type(proxies) == list:
            for proxy in proxies:
                self.__proxyCheck(proxy, session, URL, TIMEOUT, details)
            print(finishedMsg)
            if len(self.__proxysSuccess) == 0 :
                print("None of the proxies you provided are working.")
            else :
                return self.__proxysSuccess
        elif type(proxies) == str:
            self.__proxyCheck(proxies, session, URL, TIMEOUT, details)
            print(finishedMsg)
            if len(self.__proxysSuccess) == 0 :
                print("Proxy address not working.")
            else :
                return self.__proxysSuccess[0]
        
    def __proxyCheck(self, proxy, session, URL, timeout, details):
        protocols = ["http","socks4","socks5"]
        if details == True:
            for protocol in protocols:
                try :
                    start = time.time()
                    session.get(URL, proxies={'https':f"{protocol}://{proxy}", "http":f"{protocol}://{proxy}"}, timeout=timeout,allow_redirects=True)
                    timeOut = (time.time() - start)
                    print(clr.setColor(40)+f"Protocol : {protocol} - Connection Successfull - {proxy}"+reset)
                    self.__proxysSuccess.append(proxy)
                    print(self.__proxy_Details(protocol,proxy,timeOut)+reset)
                    break
                except :
                    print(clr.red+f"Protocol : {protocol} - The connection is unstable - {proxy}"+reset)
                    continue
        else :
            for protocol in protocols:
                try :
                    session.get(URL, proxies={'https':f"{protocol}://{proxy}", "http":f"{protocol}://{proxy}"}, timeout=timeout,allow_redirects=True)
                    self.__proxysSuccess.append(proxy)
                except :
                    continue

    def __exceptions(self,proxies,details,url,timeout):
        if type(proxies) != list and type(proxies) != str :
            raise Exception("The proxys parameter must be a list.")
        elif str(url).find("http") == -1:
            raise Exception("The url parameter must be a link.")
        elif type(timeout) == bool or type(timeout) == str :
            raise Exception("The timeout parameter must be tuple, integer or float.")
        elif type(details) != bool:
            raise Exception("The details parameter must be true or false.")
        else :
            pass

    def __proxy_Details(self,protocol,proxy,timeOut):
        start = time.time()
        session = requests.Session()
        session.headers['User-Agent'] = self.userAgent
        session.max_redirects = 300
        getUrl = session.get("https://ipwhois.app/json/",proxies={'https':f"{protocol}://{proxy}", "http":f"{protocol}://{proxy}"},timeout=(3.05,10))
        response = getUrl.json()
        ipAddr = clr.green+response["ip"]+reset
        proxyType = clr.setColor(184)+response["type"]+reset
        country = clr.setColor(208)+response["country"]+reset
        region = clr.setColor(208)+response["region"]+reset
        userAgentGet = session.get("http://whatsmyuseragent.org/",proxies={'https':f"{protocol}://{proxy}", "http":f"{protocol}://{proxy}"},timeout=(3.05,10))
        userAgent = clr.setColor(39)+(userAgentGet.text).split("<p")[1].split("</p>")[0].split('>')[1].strip()+reset
        time_out = ((time.time() - start) + timeOut) / 3
        if time_out <= 50:
            color = clr.setColor(112)
        else :
            color = clr.red
        text = f"ProxyIp : {ipAddr} -- ProxyType : {proxyType} -- Country : {country} -- Region : {region} -- AvagereTimeOut : {color}{time_out:.2f}sn{reset}\nYour User-Agent = {userAgent}"  
        return text

    def getDefaultUseragent(self,useragent="windows"):
        """Default Useragent Values = Windows - linux - macOs - Android - Iphone - Ipad - Ipod\n
            Random UserAgent = Call the randomUserAgent() method for the random user agent."""
        defaultUseragent = {
            "Android":"Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
            "Windows":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
            "MacOS":"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
            "Linux":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
            "Iphone":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/92.0.4515.90 Mobile/15E148 Safari/604.1",
            "Ipad":"Mozilla/5.0 (iPad; CPU OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/92.0.4515.90 Mobile/15E148 Safari/604.1",
            "Ipod":"Mozilla/5.0 (iPod; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/92.0.4515.90 Mobile/15E148 Safari/604.1"}

        return defaultUseragent[useragent.capitalize()]

    def randomUserAgent(self):
        """
        randomUserAgent = Returns a random useragent when the method is called.\n
        """
        rnd = random.choice(userAgentList)
        return rnd