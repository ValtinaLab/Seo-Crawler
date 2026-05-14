import pandas as pd

from crawler import SEOCrawler


START_URL = "https://www.cinefilia.blog/"


crawler = SEOCrawler(START_URL, max_pages=10)

results = crawler.crawl()

df = pd.DataFrame(results)

df.to_csv("seo_report_v2.csv", index=False, encoding="utf-8-sig")

print(df.head())

print(f"\nPages crawled: {len(df)}")

print("SEO report generated!")