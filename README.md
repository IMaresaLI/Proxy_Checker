[![proxyCheck](https://img.shields.io/pypi/v/proxyCheck-mp?style=for-the-badge)](https://pypi.org/project/proxyCheck-mp/)
[![Python3](https://img.shields.io/pypi/pyversions/proxyCheck-mp?style=for-the-badge)](https://www.python.org/downloads/release/python-396/)
[![proxyCheck](https://img.shields.io/github/languages/code-size/IMaresaLI/Proxy_Checker?style=for-the-badge)](https://pypi.org/project/proxyCheck-mp/)
[![proxyCheck](https://img.shields.io/pypi/l/proxyCheck-mp?style=for-the-badge)](https://github.com/IMaresaLI/Proxy_Checker/blob/lastversion/LICENSE)

# Proxy Checker Mp

# How to use ?

## 1-) Module Install and Import
 - **Install Module**
```python
pip install proxyCheck-mp
```
```python
pip3 install proxyCheck-mp
```
- **Import Module**
```python
from proxyChecker import ProxyController
```
## 2-) proxyController class must be called.
```python
prxCont = ProxyController()
```
## 3-) User-agent default value and reassign.

**Default Value ;**
```python
getDefaultUseragent() --> "windows" 
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
```
**Assigning a new value ;**
```python
prxCont = ProxyController()
#First method
prxCont.userAgent = 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'

#Second method
prxCont.userAgent = getDefaultUseragent("linux") --> linux user-agent
#Operating systems defined in the getDefaultUseragent() method. --> Windows,Linux,Macos,Android,Iphone,Ipad,Ipod

#Third method
prxCont.userAgent = randomUserAgent() --> a random user-agent
# When this method calls, it fetches a random user agent from the Eight Thousand-element list.
```
## 3-) The proxyControl method bound to the proxyController class must be called.
### prxCont.proxyControl(proxys , url , timeout , max_redirects, details)
```
Parameter Details ;
proxies  -> Proxies parameter must be list or str. (List or String)
url	-> Give url to check proxy. (https-http) Default = https://www.google.com
timeout -> Set a waiting time to connect. Default timeout = (3.05,27) >> (connect,read)
max_redirects -> Determines whether redirects are used. Default max_redirects = (False,300) >> (use,value)
details -> Information message about whether the proxy is working or not. (True or False) Default = True
```
## 4-) Output - Successfull
```python
prxCont = ProxyController()
prxCont.userAgent = prxCont.randomUserAgent()

# Singular
proxy = "117.251.103.186:8080"
responce = prxCont.proxyControl(proxy)
print(responce)

#output _> 
	ProxyIp : 117.251.103.186 -- ProxyType : IPv4 -- Country : India -- Region : Chandigarh -- AvagereTimeOut : 1.26sn
	Your User-Agent =  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36
	Protocol : http - Connection Successfull - 117.251.103.186
	
	RESPONCE :
	{'Proxy': '117.251.103.186', 'ProxyType': 'IPv4', 'Protocol': 'http', 'Country': 'India', 'Region': 'Chandigarh', 'AvagereTimeOut': 1.2850966453552246, 'Color': '\x1b[38;5;112m', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

responce = prxCont.proxyControl(proxy,detail=False)
print(responce)
#output2 _>
	RESPONCE :
	{'Proxy': '117.251.103.186', 'ProxyType': 'IPv4', 'Protocol': 'http', 'Country': 'India', 'Region': 'Chandigarh', 'AvagereTimeOut': 1.2850966453552246, 'Color': '\x1b[38;5;112m', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

# Multiple
proxies = ["117.251.103.186:8080","178.48.68.61:4145","181.215.178.39:1337"]
responce = prxCont.proxyControl(proxies)
print(responce)

#output _> 
	ProxyIp : 178.48.68.61:4145 -- ProxyType : IPv4 -- Country : Hungary -- Region : Western Transdanubia -- AvagereTimeOut : 0.89sn      
	Your User-Agent =  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36
	Protocol : socks4 - Connection Successfull - 178.48.68.61:4145
	ProxyIp : 181.215.178.39:1337 -- ProxyType : IPv4 -- Country : United Arab Emirates -- Region : Abu Dhabi Emirate -- AvagereTimeOut : 0.67sn
	Your User-Agent =  Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36      
	Protocol : http - Connection Successfull - 181.215.178.39:1337
	
	RESPONCE :
	[{'Proxy': '178.48.68.61:4145', 'ProxyType': 'IPv4', 'Protocol': 'socks4', 'Country': 'Hungary', 'Region': 'Western Transdanubia', 'AvagereTimeOut': 0.8949407736460367, 'Color': '\x1b[38;5;112m', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}, {'Proxy': '181.215.178.39:1337', 'ProxyType': 'IPv4', 'Protocol': 'http', 'Country': 'United Arab Emirates', 'Region': 'Abu Dhabi Emirate', 'AvagereTimeOut': 0.6718703111012777, 'Color': '\x1b[38;5;112m', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}]
	
proxies = ["117.251.103.186:8080","178.48.68.61:4145","181.215.178.39:1337"]
responce = prxCont.proxyControl(proxies,details=False)
print(responce)
#output2 _>
	RESPONCE :
	[{'Proxy': '178.48.68.61:4145', 'ProxyType': 'IPv4', 'Protocol': 'socks4', 'Country': 'Hungary', 'Region': 'Western Transdanubia', 'AvagereTimeOut': 0.8949407736460367, 'Color': '\x1b[38;5;112m', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}, {'Proxy': '181.215.178.39:1337', 'ProxyType': 'IPv4', 'Protocol': 'http', 'Country': 'United Arab Emirates', 'Region': 'Abu Dhabi Emirate', 'AvagereTimeOut': 0.6718703111012777, 'Color': '\x1b[38;5;112m', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}]

```
## 4-) Output - UnSuccessful
```python
prxCont = ProxyController()
proxies = ["0.0.0.0:18","1.1.1.1:80","11.11.11.11:8080"]
responce = prxCont.proxyControl(proxies)
print(responce)
#output _> 
	The connection is unstable - 0.0.0.0:18
	The connection is unstable - 1.1.1.1:80
	The connection is unstable - 11.11.11.11:8080
	None
	
proxies = ["0.0.0.0:18","1.1.1.1:80","11.11.11.11:8080"]
responce = prxCont.proxyControl(proxies,details=False)
print(responce)
#output2 _>
	None
```