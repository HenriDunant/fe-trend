import pandas as pd
import requests
from bs4 import BeautifulSoup

from article_parser import extract_article_metadata
from fuel_parser import extract_fuel_economy
from vehicle_parser import extract_vehicle_identity
from model_parser import load_model_reference, extract_model_trim
from conversions import add_metric_conversions


urls = [
    "https://www.caranddriver.com/reviews/a73308571/2027-rivian-r2-performance-awd-launch-edition-test/",
    "https://www.caranddriver.com/reviews/a71430685/2025-porsche-911-carrera-4-gts-cabriolet-test/",
    "https://www.caranddriver.com/reviews/a73347571/2026-toyota-rav4-gr-sport-plug-in-hybrid-test/",
    "https://www.caranddriver.com/reviews/a70303382/2026-porsche-macan-gts-ev-drive/"
]


model_reference = load_model_reference()

records = []

errors = []

for url in urls:

    print("Processing:", url)

    try:
        response = requests.get(
            url,
            timeout=30
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        page_text = soup.get_text(
            " ",
            strip=True
        )

        article_data = extract_article_metadata(
            soup,
            url
        )

        cd_start = page_text.find(
            "C/D FUEL ECONOMY"
        )

        epa_start = page_text.find(
            "EPA FUEL ECONOMY"
        )

        if cd_start == -1 or epa_start == -1:
            errors.append({
                "url": url,
                "error_type": "Missing fuel section",
                "details": "C/D or EPA fuel economy section not found"
            })

            continue

        cd_section = page_text[
            cd_start:epa_start
        ]

        epa_end = page_text.find(
            "C/D TESTING EXPLAINED",
            epa_start
        )

        if epa_end == -1:
            epa_end = len(page_text)

        epa_section = page_text[
            epa_start:epa_end
        ]

        fuel_data = extract_fuel_economy(
            cd_section,
            epa_section
        )

        vehicle_identity = extract_vehicle_identity(
            article_data["vehicle_name"]
        )

        model_data = extract_model_trim(
            vehicle_identity["make"],
            vehicle_identity["model_trim"],
            model_reference
        )

        vehicle_record = {
            **article_data,
            **vehicle_identity,
            **model_data,
            **fuel_data,
        }

        metric_data = add_metric_conversions(
            vehicle_record
        )

        vehicle_record.update(
            metric_data
        )

        records.append(
            vehicle_record
        )

    except Exception as error:

        errors.append({
            "url": url,
            "error_type": type(error).__name__,
            "details": str(error)
        })

        print("Failed:", error)

# Convert all records into one DataFrame
df = pd.DataFrame(records)

print("\n--- DATASET ---")
print(df.to_string(index=False))


# Save dataset
df.to_csv(
    "data/processed/vehicle_dataset.csv",
    index=False
)

print(
    "\nSaved:",
    "data/processed/vehicle_dataset.csv"
)

error_df = pd.DataFrame(errors)

error_df.to_csv(
    "data/processed/error_log.csv",
    index=False
)

print(
    "Saved:",
    "data/processed/error_log.csv"
)

print("\n--- SUMMARY ---")
print("Successful records:", len(records))
print("Errors:", len(errors))