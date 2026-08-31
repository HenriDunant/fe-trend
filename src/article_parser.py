import re


def extract_article_metadata(soup, url):

    data = {
        "article_title": None,
        "vehicle_name": None,
        "model_year": None,
        "article_date": None,
        "source_url": url,
    }

    # ---------------------------------
    # Article headline
    # ---------------------------------
    heading = soup.find("h1")

    if heading:
        data["article_title"] = heading.get_text(
            " ",
            strip=True
        )

    # ---------------------------------
    # Convert webpage to readable text
    # ---------------------------------
    page_text = soup.get_text(" ", strip=True)

    # ---------------------------------
    # Vehicle name from Specifications
    # ---------------------------------
    match = re.search(
        r"Specifications\s+(?:Specifications\s+)?"
        r"(.+?)\s+Vehicle Type:",
        page_text,
        re.IGNORECASE,
    )

    if match:
        data["vehicle_name"] = match.group(1).strip()

    # ---------------------------------
    # Model year
    # Prefer vehicle_name over headline
    # ---------------------------------
    if data["vehicle_name"]:
        match = re.search(
            r"\b(20\d{2})\b",
            data["vehicle_name"]
        )

        if match:
            data["model_year"] = int(match.group(1))

    # ---------------------------------
    # Publication date
    # ---------------------------------
    published = soup.find(
        "meta",
        attrs={"property": "article:published_time"}
    )

    if published:
        data["article_date"] = published.get("content")

    return data