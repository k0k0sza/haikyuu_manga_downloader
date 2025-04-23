from glob import glob
import os.path as path
import os
from PIL import Image

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

imgs1 = []
for file in os.listdir():
    if file.endswith(".jpg"):
        imgs.append(file)

save_as_pdf(files=imgs1, out='images.pdf')
