import requests 

def get_url(line):
    return line.split(",")[0].split(": ")[1]

lines = None 
with open('../Unlimited Memory.txt', 'r') as f:
    lines = f.readlines() 

urls = []
for line in lines: 
    urls.append(get_url(line))

for index, url in enumerate(urls):
    print(f"Checking page {index}...")
    res = requests.get(url)
    if res.status_code != 200:
        print(f"{index}: {url}")
        input()
        
for index, url in enumerate([]):
    print(f"Checking page {index}...")
    res = requests.get(url)
    if res.status_code != 200:
        print(f"{index}: {url}")
        input()
