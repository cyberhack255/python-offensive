import requests
import random
import string

url = "https://pentestingkb.softnetsolutions.com.au"
characters = string.ascii_letters + string.digits

for i in range(3):
    random_char =''.join(random.choice(characters) for i in range(10))
    response = requests.get(f"{url}/{random_char}")
    # process response
    print(random_char)