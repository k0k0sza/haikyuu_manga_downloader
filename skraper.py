import requests
from bs4 import BeautifulSoup 


url = "https://w1.readhaikyu.online/manga/haikyuu-chapter-69/"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like GEcko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

r = requests.get(url=url, headers=headers)
soup = BeautifulSoup(r.content, "html.parser")
imgs = soup.find_all("div", {"class": "separator"})
rows = soup.find_all('img')

for im in imgs:
    src = im.img['src']
    new_img = requests.get(src, headers=headers)
    file_name = src.split("/")[-1]
    print(file_name)
    if new_img.status_code != 200:
        print("error")
    else:
        with open(file_name, "wb") as f:
            noop = f.write(new_img.content)
            print("SAVE {}".format(file_name))
