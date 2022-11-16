import requests,time,random
from syscolors.sysColors import SystemColors
from proxyChecker.userAgentData import *

clr = SystemColors()
reset = clr.reset

class ProxyController:
    def __init__(self):
        self.__proxysSuccess = []
        self.userAgent = self.getDefaultUseragent()
   
    def __sessionOpen(self):
        self.session = requests.Session()
        self.session.headers['User-Agent'] = self.userAgent
        requests.exceptions.RequestsWarning()
        
    def proxyControl(self,proxies,url="https://www.google.com",timeout=(3.05,27),max_redirects=(False,300),details=True):
        """You should send the proxy list you want to check.\n
        proxies  : Proxies parameter must be list or str. (List or String)\n
        url     : Give url to check proxy. (https-http)\n
        timeout : Set a waiting time to connect. Default timeout = (3.05,27) >> (connect,read)\n
        max_redirects : Determines whether redirects are used. Default max_redirects = (False,300) >> (use,value)\n
        details : Information message about whether the proxy is working or not. (True or False)\n
        User Agent : You can find it by typing my user agent into Google.\n
        Default User Agent : Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36"""
        try:
            self.__exceptions(proxies,details,url,timeout)
        except Exception as err :
            return print("Error :: > "+str(err))
        URL = url
        TIMEOUT = timeout
        if max_redirects[0] :
            self.session.max_redirects = max_redirects[1]

        if type(proxies) == list:
            for proxy in proxies:
                self.__sessionOpen()
                proxy_responce = self.__proxyCheck(proxy, self.session, URL, TIMEOUT, details)
                if proxy_responce :
                    self.__proxysSuccess.append(proxy_responce)
                self.session.close()
            if len(self.__proxysSuccess) == 0 :
                return None
            else :
                return self.__proxysSuccess
            
        elif type(proxies) == str:
            self.__sessionOpen()
            proxy_responce = self.__proxyCheck(proxies, self.session, URL, TIMEOUT, details)
            self.session.close()
            if proxy_responce :
                return proxy_responce
            else :
                return None
        
    def __proxyCheck(self, proxy, session, URL, timeout, details):
        success = False
        data = {}
        protocols = ["http","socks4","socks5"]
        for protocol in protocols:
            try :
                start = time.time()
                session.get(URL, proxies={"http":f"{protocol}://{proxy}", "https":f"{protocol}://{proxy}"}, timeout=timeout,verify=True, allow_redirects=True)
                timeOut = (time.time() - start)
                success = True
                data.update({"Protocol":protocol,"Proxy":proxy,"TimeOut":timeOut})
                break
            except:
                try :
                    start = time.time()
                    session.get(URL, proxies={'https':f"{protocol}://{proxy}", "http":f"{protocol}://{proxy}"}, timeout=timeout,verify=False,allow_redirects=True)
                    timeOut = (time.time() - start)
                    success = True
                    data.update({"Protocol":protocol,"Proxy":proxy,"TimeOut":timeOut})
                    break
                except :
                    pass
        if success :
            dt = self.__proxy_Details(protocol,proxy,timeOut)
            if details :
                self.__details(dt)
                return dt
            else :
                return dt
        else :
            if details :
                print(clr.red+f"The connection is unstable - {proxy}"+reset)
            return None       
        
    def __details(self,dt):
        text = f"ProxyIp : {clr.green}{dt['Proxy']}{reset} -- ProxyType : {clr.setColor(184)}{dt['ProxyType']}{reset} -- Country : {clr.setColor(208)}{dt['Country']}{reset} -- Region : {clr.setColor(208)}{dt['Region']}{reset} -- AvagereTimeOut : {dt['Color']}{dt['AvagereTimeOut']:.2f}sn{reset}\nYour User-Agent = {clr.setColor(39)} {dt['user-agent']}"+reset  
        print(text)
        print(clr.setColor(40)+f"Protocol : {dt['Protocol']} - Connection Successfull - {dt['Proxy']}"+reset)

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
        try :
            start = time.time()
            session = requests.Session()
            session.headers['User-Agent'] = self.userAgent
            requests.exceptions.RequestsWarning()
            try :
                getUrl = session.get("https://ipwhois.app/json/",proxies={'https':f"{protocol}://{proxy}", "http":f"{protocol}://{proxy}"},timeout=(3.05,10),verify=True, allow_redirects=True)
            except :
                getUrl = session.get("https://ipwhois.app/json/",proxies={'https':f"{protocol}://{proxy}", "http":f"{protocol}://{proxy}"},timeout=(3.05,10),verify=False, allow_redirects=True)
            response = getUrl.json()
            ipAddr = response["ip"]
            proxyType = response["type"]
            country = response["country"]
            region = response["region"]
            time_out = ((time.time() - start) + timeOut) / 3
            if time_out <= 50:
                color = clr.setColor(112)
            else :
                color = clr.red
            Proxy_data = {"Proxy":proxy,"ProxyType":proxyType,"Protocol":protocol,"Country":country,"Region":region,"AvagereTimeOut":time_out,"Color":color,"user-agent":self.userAgent} 
        except :
            time_out = ((time.time() - start) + timeOut) / 3
            if time_out <= 50:
                color = clr.setColor(112)
            else :
                color = clr.red
            Proxy_data = {"Proxy":proxy,"ProxyType":None,"Protocol":protocol,"Country":None,"Region":None,"AvagereTimeOut":time_out,"Color":color,"user-agent":self.userAgent} 

        return Proxy_data

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