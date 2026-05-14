def generate_summary(df, issues_df):

    summary = {
        "pages_crawled": len(df),

        "missing_titles": len(
            issues_df[
                issues_df["issue"] == "Missing title"
            ]
        ),

        "missing_h1": len(
            issues_df[
                issues_df["issue"] == "Missing H1"
            ]
        ),

        "missing_meta_descriptions": len(
            issues_df[
                issues_df["issue"] ==
                "Missing meta description"
            ]
        ),

        "duplicate_titles": len(
            issues_df[
                issues_df["issue"] ==
                "Duplicate title"
            ]
        )
    }

    return summary