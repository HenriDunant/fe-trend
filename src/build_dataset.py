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
]


model_reference = load_model_reference()

records = []


for url in urls:

    print("Processing:", url)

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

    # Article metadata
    article_data = extract_article_metadata(
        soup,
        url
    )

    # Locate fuel economy sections
    cd_start = page_text.find(
        "C/D FUEL ECONOMY"
    )

    epa_start = page_text.find(
        "EPA FUEL ECONOMY"
    )

    if cd_start == -1 or epa_start == -1:
        print("Fuel economy section missing.")
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

    # Fuel data
    fuel_data = extract_fuel_economy(
        cd_section,
        epa_section
    )

    # Vehicle identity
    vehicle_identity = extract_vehicle_identity(
        article_data["vehicle_name"]
    )

    # Model / trim
    model_data = extract_model_trim(
        vehicle_identity["make"],
        vehicle_identity["model_trim"],
        model_reference
    )

    # Build base record
    vehicle_record = {
        **article_data,
        **vehicle_identity,
        **model_data,
        **fuel_data,
    }

    # Metric conversions
    metric_data = add_metric_conversions(
        vehicle_record
    )

    vehicle_record.update(
        metric_data
    )

    records.append(
        vehicle_record
    )


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