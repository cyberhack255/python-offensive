import requests
import threading

urls = [
    "https://pentestingkb.softnetsolutions.com.au",
    # ... add more URLs as needed
]

def make_request(url):
    response = requests.get(url)
    print (response)
    # process response

threads = []
for url in urls:
    thread = threading.Thread(target=make_request, args=(url,))
    thread.start()
    threads.append(thread)
    if len(threads) >= 200:
        for thread in threads:
            thread.join()
        threads = []

for thread in threads:
    thread.join()