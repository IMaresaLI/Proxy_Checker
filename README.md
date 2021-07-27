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
from proxyChecker.proxyCheck import ProxyController
```
## 2-) proxyController class must be called.
```python
prxCont = ProxyController()
```
## 3-) User-agent default value and reassign.

**Default Value ;**
```python
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
```
**Assigning a new value ;**
```python
prxCont = ProxyController()
prxCont.userAgent = 'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
```
## 3-) The proxyControl method bound to the proxyController class must be called.
### prxCont.proxyControl(proxys , url , timeout , details)
```
Parameter Details ;
proxies  -> Proxies parameter must be list or str. (List or String)
url	-> Give url to check proxy. (https-http) Default = https://www.google.com
timeout -> Set a waiting time to connect. Default timeout = (3.05,27) >> (connect,read)
details -> Information message about whether the proxy is working or not. (True or False) Default = True
```
## 4-) Output - Positive
```python
prxCont = ProxyController()
proxy = '52.143.130.19:3128'
print(prxCont.proxyControl(proxy))
#output _> 
	Protocol : http - Connection Successfull - 52.143.130.19:3128
	proxyIp : 52.143.130.19 -- proxyType : IPv4 -- country : France -- timeOut : 0.43 second
	Proxy check completed.
	52.143.130.19:3128

print(prxCont.proxyControl(proxyList,detail=False))
#output2 _>
	Proxy check completed.
	52.143.130.19:3128
```
## 4-) Output - Negative
```python
prxCont = ProxyController()
proxyList = ["0.0.0.0:18","1.1.1.1:80","11.11.11.11:8080"]
prxCont.proxyControl(proxyList)
#output _> 
	Protocol : http - The connection is unstable - 0.0.0.0:18
	Protocol : socks4 - The connection is unstable - 0.0.0.0:18
	Protocol : socks5 - The connection is unstable - 0.0.0.0:18
	Protocol : http - The connection is unstable - 1.1.1.1:80
	Protocol : socks4 - The connection is unstable - 1.1.1.1:80
	Protocol : socks5 - The connection is unstable - 1.1.1.1:80
	Protocol : http - The connection is unstable - 11.11.11.11:8080
	Protocol : socks4 - The connection is unstable - 11.11.11.11:8080
	Protocol : socks5 - The connection is unstable - 11.11.11.11:8080
	Proxy check completed.
	None of the proxies you provided are working.
	
prxCont.proxyControl(proxyList,detail=False)
#output2 _>
	Proxy check completed.
	None of the proxies you provided are working.
```
