from requests import get
from bs4 import BeautifulSoup
from datetime import datetime as dt
from os import listdir, makedirs
from shutil import copyfileobj
from urllib.parse import urlparse
from base64 import b64decode
import re


def scrap_text(url):
    raw_page = get(url)
    soup = BeautifulSoup(raw_page.text, 'html.parser')

    for script in soup(["script", "style"]):
        script.decompose()
    lines = (line.strip() for line in soup.html.body.text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = "\n".join(chunk for chunk in chunks if chunk)

    save_url = url.split("//")[-1]
    if save_url not in listdir("data"):
        makedirs(f"data/{save_url}", exist_ok = True)

    with open(f"data/{save_url}/text", 'w') as f:
        f.write(text)


def download_images(url):
    string = get(url).text
    soup = BeautifulSoup(string, 'html.parser')
    host = '{uri.scheme}://{uri.netloc}/'.format(uri = urlparse(url))[:-1]

    bcg_img = [m.group(1) for m in re.finditer("""url\(['"](.*)['"]\)""", string)\
        if m.group(1) != '']
    with open('out', 'w') as f:
        f.write(str(bcg_img))

    save_url = url.split("//")[-1]
    if save_url not in listdir("data"):
        makedirs(f"data/{save_url}", exist_ok = True)
    if "images" not in listdir(f"data/{save_url}"):
        makedirs(f"data/{save_url}/images", exist_ok = True)

    for img_src in bcg_img:
        response = get(host + img_src, stream = True)
        if response.status_code == 200:
            save_img_name = img_src.split("/")[-1]
            with open(f"data/{save_url}/images/{save_img_name}", 'wb') as f:
                f.write(response.content)

    i = 1
    for img_tag in soup.find_all('img'):
        if not ";base64," in img_tag['src']:
            if not 'http' in img_tag['src']:
                response = get(host + img_tag['src'], stream = True)
            else:
                response = get(img_tag['src'], stream = True)
            if response.status_code == 200:
                save_img_name = img_tag['src'].split("/")[-1]
                with open(f"data/{save_url}/images/{save_img_name}", 'wb') as f:
                    f.write(response.content)
        else:
            bytes = b64decode(img_tag['src'].split(';base64,')[-1])
            with open(str(i), 'wb') as f:
                f.write(bytes)
            i =+ 1
