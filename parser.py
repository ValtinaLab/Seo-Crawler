from bs4 import BeautifulSoup


def clean_text(text):

    if not text:
        return None

    return " ".join(text.strip().split())


def parse_html(url, html):

    soup = BeautifulSoup(html, "lxml")

    title = clean_text(soup.title.text) if soup.title else None

    h1 = clean_text(soup.h1.text) if soup.h1 else None

    meta = soup.find("meta", attrs={"name": "description"})

    description = clean_text(meta["content"]) if meta else None

    # NEW: images without ALT
    images = soup.find_all("img")

    missing_alt = 0

    for img in images:

        if not img.get("alt"):

            missing_alt += 1

    return {
        "url": url,
        "title": title,
        "h1": h1,
        "meta_description": description,
        "images_missing_alt": missing_alt
    }