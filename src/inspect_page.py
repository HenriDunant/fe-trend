from article_parser import extract_article_metadata

import sys

import requests
from bs4 import BeautifulSoup

from fuel_parser import extract_fuel_economy

# -------------------------------------------------
# Extract URL from the terminal

if len(sys.argv) < 2:
    print("Usage: python src\\inspect_page.py <URL>")
    sys.exit(1)

url = sys.argv[1]

print("URL being tested:", url)

# -------------------------------------------------
# Download webpage

response = requests.get(
    url,
    timeout=30
)

response.raise_for_status()

# -------------------------------------------------
# Convert HTML into readable text

soup = BeautifulSoup(response.text, "html.parser")
page_text = soup.get_text(" ", strip=True)

article_data = extract_article_metadata(
    soup,
    url
)

# -------------------------------------------------
# Locate fuel-economy sections

cd_start = page_text.find("C/D FUEL ECONOMY")
epa_start = page_text.find("EPA FUEL ECONOMY")

if cd_start == -1:
    print("C/D FUEL ECONOMY section not found.")
    sys.exit(1)

if epa_start == -1:
    print("EPA FUEL ECONOMY section not found.")
    sys.exit(1)


cd_section = page_text[cd_start:epa_start]

# -------------------------------------------------
# Locate end of EPA section

epa_end = page_text.find("C/D TESTING EXPLAINED", epa_start)

if epa_end == -1:
    epa_end = len(page_text)

epa_section = page_text[epa_start:epa_end]


# -------------------------------------------------
# Extract structured values


fuel_data = extract_fuel_economy(
    cd_section,
    epa_section
)


article_data = extract_article_metadata(
    soup,
    url
)

vehicle_record = {
    **article_data,
    **fuel_data,
}

# -------------------------------------------------
# Display results

print("Status code:", response.status_code)

print("\n--- C/D SECTION ---")
print(cd_section)

print("\n--- EPA SECTION ---")
print(epa_section)

print("\n--- EXTRACTED DATA ---")

for key, value in fuel_data.items():
    print(key, "=", value)


print("\n--- ARTICLE DATA ---")

for key, value in article_data.items():
    print(key, "=", value)

print("\n--- COMPLETE VEHICLE RECORD ---")

for key, value in vehicle_record.items():
    print(key, "=", value)