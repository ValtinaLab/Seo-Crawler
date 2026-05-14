from urllib.parse import urljoin, urlparse


def normalize_url(base, link):

    full_url = urljoin(base, link)

    parsed = urlparse(full_url)

    clean_url = (
        f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
    )

    # Remove trailing slash
    if clean_url.endswith("/"):

        clean_url = clean_url[:-1]

    return clean_url


def get_domain(url):

    return urlparse(url).netloc


def is_internal_url(url, domain):

    return urlparse(url).netloc == domain