# Proxy_Checker

# How to use ?

## 1-) Module Install and Import
 - **Install Module**
```
pip install proxyCheck-mp
```
```
pip3 install proxyCheck-mp
```
- **Import Module**
```
from proxyChecker.proxyCheck import ProxyController
```
## 1-) proxyController class must be called.
### prxCont = ProxyController()

## 2-) The proxyControl method bound to the proxyController class must be called.
### prxCont.proxyControl(proxys , url , timeout , details)

```
Parameter Details ;
proxy 	-> You have to give the list structure. (List)
url	-> Give url to check proxy. (https-http) Default = https://www.google.com
timeout -> Set a waiting time to connect. Default timeout = (3.05,27) >> (connect,read)
details -> Information message about whether the proxy is working or not. (True or False) Default = True
```
## 3- Output
```
prxCont = ProxyController()
proxyList = ["0.0.0.0:18","1.1.1.1:80","11.11.11.11:8080"]
prxCont.proxyControl(proxyList)
#output _> 
	The connection is unstable - 0.0.0.0:18
	The connection is unstable - 1.1.1.1:80
	The connection is unstable - 11.11.11.11:8080
	Proxy attempt finished.
	None of the proxies you provided are working.

prxCont.proxyControl(proxyList,detail=True)
#output2 _>
	Proxy attempt finished.
	None of the proxies you provided are working.
```
