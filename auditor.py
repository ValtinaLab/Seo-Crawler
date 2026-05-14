def audit_seo(df):

    issues = []

    for _, row in df.iterrows():

        url = row["url"]

        title = row.get("title")
        h1 = row.get("h1")
        meta = row.get("meta_description")

        # Missing title
        if not title:
            issues.append({
                "url": url,
                "issue": "Missing title"
            })

        # Title too long / short
        elif len(title) < 10 or len(title) > 60:
            issues.append({
                "url": url,
                "issue": "Title length issue"
            })

        # Missing H1
        if not h1:
            issues.append({
                "url": url,
                "issue": "Missing H1"
            })

        # Missing meta
        if not meta:
            issues.append({
                "url": url,
                "issue": "Missing meta description"
            })

        # Meta too short / long
        elif len(meta) < 50 or len(meta) > 160:
            issues.append({
                "url": url,
                "issue": "Meta description length issue"
            })

        # Thin content (very basic )
        if title and h1:
            if len(title + h1) < 30:
                issues.append({
                    "url": url,
                    "issue": "Thin content (basic check)"
                })

    return issues