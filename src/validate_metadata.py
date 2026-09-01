from model_parser import (
    load_model_reference,
    extract_model_trim,
)

from vehicle_parser import extract_vehicle_identity

import requests
from bs4 import BeautifulSoup

from article_parser import extract_article_metadata


urls = [
    "https://www.caranddriver.com/reviews/a73308571/2027-rivian-r2-performance-awd-launch-edition-test/",
    "https://www.caranddriver.com/reviews/a71430685/2025-porsche-911-carrera-4-gts-cabriolet-test/",
    "https://www.caranddriver.com/reviews/a73347571/2026-toyota-rav4-gr-sport-plug-in-hybrid-test/",
]

model_reference = load_model_reference()

for url in urls:

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    article_data = extract_article_metadata(
        soup,
        url
    )

    vehicle_identity = extract_vehicle_identity(
        article_data["vehicle_name"]
    )

    model_data = extract_model_trim(
        vehicle_identity["make"],
        vehicle_identity["model_trim"],
        model_reference,
    )

    print("\n--------------------------------")
    print("Vehicle:", article_data["vehicle_name"])
    print("Make:", vehicle_identity["make"])
    print("Model:", model_data["model"])
    print("Trim:", model_data["trim"])
    print("Model Year:", article_data["model_year"])
    print("--------------------------------")