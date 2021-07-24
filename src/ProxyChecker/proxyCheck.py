import requests,colorama
from colorama.ansi import Fore

colorama.init(autoreset=True)

class ProxyController:
    def __init__(self):
        self.__proxysSuccess = []
        self.__proxysUnsuccess = []

    def proxyControl(self,proxys,url="https://www.google.com",timeout=(3.05,27),details=True):
        """You should send the proxy list you want to check.\n
        proxys : You have to give the list structure. (List)\n
        url     : Give url to check proxy. (https-http)\n
        timeout : Set a waiting time to connect. Default timeout = (3.05,27) >> (connect,read)\n
        details : Information message about whether the proxy is working or not. (True or False)"""
        try:
            self.__exceptions(proxys,details,url,timeout)
        except Exception as err :
            return print("Error :: > "+str(err))
        URL = url
        TIMEOUT = timeout
        session = requests.Session()
        session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
        session.max_redirects = 300
        for proxy in proxys:
            self.__proxyCheck(proxy, session, URL, TIMEOUT, details)
        print("Proxy attempt finished.")
        if len(self.__proxysSuccess) == 0 :
            print("None of the proxies you provided are working.")
        else :
            return self.__proxysSuccess 


    def __proxyCheck(self, proxy, session, URL, TIMEOUT, details):
        if details == True:
            try :
                session.get(URL, proxies={'https':"http://"+proxy, "http":"http://"+proxy}, timeout=TIMEOUT,allow_redirects=True)
                print(Fore.LIGHTGREEN_EX+"Connection Successfull - %s" %(proxy))
                self.__proxysSuccess.append(proxy)
            except :
                print(Fore.LIGHTRED_EX+"The connection is unstable - %s" %(proxy))
                self.__proxysUnsuccess.append(proxy)
        else :
            try :
                session.get(URL, proxies={'https':"http://"+proxy, "http":"http://"+proxy}, timeout=TIMEOUT,allow_redirects=True)
                self.__proxysSuccess.append(proxy)
            except :
                self.__proxysUnsuccess.append(proxy)

    def __exceptions(self,proxys,details,url,timeout):
        if type(proxys) != type([]) :
            raise Exception("The proxys parameter must be a list.")
        elif str(url).find("http") == -1:
            raise Exception("The url parameter must be a link.")
        elif type(timeout) == type(True) or type(timeout) == type("") :
            raise Exception("The timeout parameter must be tuple, integer or float.")
        elif type(details) != type(True):
            raise Exception("The details parameter must be true or false.")
        else :
            pass


