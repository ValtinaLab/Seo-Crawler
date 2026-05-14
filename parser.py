from bs4 import BeautifulSoup

def parse_html(url, html):

    soup = BeautifulSoup(html, "lxml")

    title = soup.title.text.strip() if soup.title else None

    h1 = soup.h1.text.strip() if soup.h1 else None

    meta = soup.find("meta", attrs={"name": "description"})

    description = meta["content"].strip() if meta else None

    return {
        "url": url,
        "title": title,
        "h1": h1,
        "meta_description": description
    }