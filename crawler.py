import requests

from bs4 import BeautifulSoup

from collections import deque

from parser import parse_html

from utils import normalize_url, is_internal_url


class SEOCrawler:

    def __init__(self, start_url, max_pages=20):

        self.start_url = start_url

        self.domain = start_url

        self.max_pages = max_pages

        self.visited = set()

        self.queue = deque([(start_url, 0)])

        self.results = []

    def crawl(self):

        while self.queue and len(self.visited) < self.max_pages:

            url, depth = self.queue.popleft()

            if url in self.visited:
                continue

            try:

                print(f"Crawling: {url}")

                response = requests.get(url, timeout=5)

                self.visited.add(url)

                if "text/html" not in response.headers.get("Content-Type", ""):
                    continue

                seo_data = parse_html(url, response.text)

                seo_data["status_code"] = response.status_code

                seo_data["depth"] = depth

                self.results.append(seo_data)

                soup = BeautifulSoup(response.text, "lxml")

                for link in soup.find_all("a"):

                    href = link.get("href")

                    if href:

                        full_url = normalize_url(url, href)

                        if is_internal_url(full_url, self.domain):

                            self.queue.append((full_url, depth + 1))

            except Exception as e:

                print(f"Error: {url} -> {e}")

        return self.results