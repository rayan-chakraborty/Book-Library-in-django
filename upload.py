import requests, base64, json, os 

def upload(filename):
    key = "b6959703bc710cc3740e1a4b69b10dab"
    api_endpoint = f"https://api.imgbb.com/1/upload?key={key}"
    with open(f'pages/{filename}', 'rb') as f:
        data = {
            "image": base64.b64encode(f.read()),
        }
        res = requests.post(url = api_endpoint, data = data )

        res = json.loads(res.text)
        return (res['data']['display_url'], res['data']['thumb']['url'], res['data']['delete_url'])




images = os.listdir('pages')
data = ''

for index, img in enumerate(images):
    print(f"Uploading {img}...")
    display_url, thumb_url, delete_url = upload(img)
    print("Done")
    data = data + f"{index+1},{display_url},{thumb_url},{delete_url}\n"

book_name = "What Women Want In A Man How To Become The Alpha Male Women Respect, Desire, And Want To Submit To"
with open(f'{book_name}.txt', 'w') as f:
    f.write(data)