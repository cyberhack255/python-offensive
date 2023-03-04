import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import random
import string
import threading
import concurrent.futures

num_requests = 10
payload ={}
if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print("[-] Usage: %s <url> " % sys.argv[1])
        sys.exit(-1)
uri = "/"
#headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile windows3.5/535.77", "X-Forwarded-for": "2.2.2.2"
            
#}
headers = {"User-Agent": "WindowsXP", "X-Forwarded-for": "4.4.8.8"}


#Define random strings
for r in range (num_requests):
    random_char = string.hexdigits
    result_str = ''.join(random.choice(random_char) for i in range(100))
    r = requests.post(url + uri + result_str, json=payload, headers=headers, verify=False)

    print(result_str)
    print(r)
    print(headers)
with concurrent.futures.ThreadPoolExecutor(max_workers=num_requests) as executor:
    results = executor.map(r, range(num_requests))

    
