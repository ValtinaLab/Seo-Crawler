from urllib.parse import urljoin, urlparse

def normalize_url(base, link):
    return urljoin(base, link)

def is_internal_url(url, domain):
    return domain in urlparse(url).netloc