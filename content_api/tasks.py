from requests import get
from bs4 import BeautifulSoup
from datetime import datetime as dt
from os import listdir, mkdir
from shutil import copyfileobj


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
        mkdir(f"data/{save_url}")

    with open(f"data/{save_url}/text", 'w') as f:
        f.write(text)

def download_images(url):
    soup = BeautifulSoup(get(url).text, 'html.parser')

    save_url = url.split("//")[-1]
    if save_url not in listdir("data"):
        mkdir(f"data/{save_url}")
    if "images" not in listdir(f"data/{save_url}"):
        mkdir(f"data/{save_url}/images")

    for img_tag in soup.find_all('img'):
        response = get(img_tag['src'], stream = True)
        if response.status_code == 200:
            save_img_name = img_tag['src'].split("/")[-1]
            with open(f"data/{save_url}/images/{save_img_name}", 'wb') as f:
                f.write(response.content)
