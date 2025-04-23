import requests
from bs4 import BeautifulSoup 
from glob import glob
import os.path as path
import os
from PIL import Image
import time
import PyPDF2
import sys

start_time = time.perf_counter()
def convert(img):
    if img.mode == 'RGBA':
        rgb = Image.new('RGB', img.size, (255,255,255)) 
        rgb.paste(img, mask=img.split()[3])
        return(rgb)
    else:
        return(img)

def save_as_pdf(files=None, out='images.pdf'):
    if files is None:
        files = glob('*.png') 
    else:
        for i in files:
            if not path.isfile(i):
                raise FileNotFoundError(f'{i} does not exist')

    if path.isfile(out):
        raise FileExistsError(f'{out} already exists.')

    images = [Image.open(i) for i in files]
    images = [convert(i) for i in images]
    images[0].save(
        out,
        'PDF',
        resolution=100.00,
        save_all=True,
        append_images=images[1:]
    )
    return(True)

def savendel():
    out1 = str(num)+".pdf"
    save_as_pdf(files=imgs, out=out1)
2
    print("SAVE PDF ")
    for img in imgs:
        os.remove(img) 
    print("DELETED")

def merge():
    merger = PyPDF2.PdfMerger()

    for file in os.listdir(os.curdir):
        if file.endswith(".pdf"):
            merger.append(file)
    merger.write(str(num1)+"-"+str(num2)+".pdf")



url1 = "https://w1.readhaikyu.online/manga/haikyuu-chapter-"
num1 = int(input("range from: "))
num2 = int(input("range to: "))
for num in range(num1,num2+1):
    print(num)
    url = url1+str(num)+"/"
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like GEcko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}

    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    imgs = soup.find_all("div", {"class": "separator"})
    rows = soup.find_all('img')

    for im in imgs:
        src = im.img['src']
        new_img = requests.get(src, headers=headers)
        file_name = src.split("/")[-1]
        if new_img.status_code != 200:
            print("error")
        else:
            with open(file_name, "wb") as f:
                noop = f.write(new_img.content)
                print("SAVE {}".format(file_name))

    imgs = []
    for file in os.listdir():
        if file.endswith(".jpg"):
            imgs.append(file)

    savendel()

end_time = time.perf_counter()

elapsed_time = end_time - start_time
merge()
print(f"Elapsed time: {elapsed_time:.1f} seconds")
    
