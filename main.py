import pandas as pd

from crawler import SEOCrawler
from auditor import audit_seo
from summary import generate_summary


START_URL = "https://www.python.org"


crawler = SEOCrawler(START_URL, max_pages=20)

results = crawler.crawl()

df = pd.DataFrame(results)

df = df.drop_duplicates(subset=["url"])

df = df.sort_values(by="depth")

df = df[
    [
        "url",
        "status_code",
        "depth",
        "title",
        "h1",
        "meta_description",
        "images_missing_alt"
    ]
]

df.to_excel("seo_report.xlsx", index=False)

issues = audit_seo(df)

issues_df = pd.DataFrame(issues)

summary = generate_summary(df, issues_df)

summary_df = pd.DataFrame([summary])

issues_df.to_excel("seo_issues.xlsx", index=False)

summary_df.to_excel("seo_summary.xlsx", index=False)

print("\nSEO SUMMARY\n")

for k, v in summary.items():

    print(f"{k}: {v}")

print("\nDONE ")