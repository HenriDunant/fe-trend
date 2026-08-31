from fuel_parser import extract_fuel_economy

import re

import requests
from bs4 import BeautifulSoup
# Import BeautifulSoup to parses the HTML


# URL Data request
url = "https://www.caranddriver.com/reviews/a73347571/2026-toyota-rav4-gr-sport-plug-in-hybrid-test/"

# Download webpage's raw HTML data.
response = requests.get(url)

# Feeds the raw HTML text into Beautiful Soup so that Python can easily interact with.
soup = BeautifulSoup(response.text, "html.parser")

# Strips away all the website's code and formatting tags
page_text = soup.get_text(" ", strip=True)

print("Status code:", response.status_code)
print("Characters received:", len(response.text))
print("C/D FUEL ECONOMY found:", "C/D FUEL ECONOMY" in page_text)
print("EPA FUEL ECONOMY found:", "EPA FUEL ECONOMY" in page_text)
print("Observed found:", "Observed:" in page_text)

cd_start = page_text.find("C/D FUEL ECONOMY")
epa_start = page_text.find("EPA FUEL ECONOMY")

cd_section = page_text[cd_start:epa_start]

print("\n--- C/D SECTION ---")
print(cd_section)

epa_start = page_text.find("EPA FUEL ECONOMY")
epa_end = page_text.find("C/D TESTING EXPLAINED")

epa_section = page_text[epa_start:epa_end]

print("\n--- EPA SECTION ---")
print(epa_section)

# Extract C/D observed MPG
observed_match = re.search(
    r"Observed:\s*(\d+)\s*(MPG|MPGe)",
    cd_section,
    re.IGNORECASE
)

if observed_match:
    cd_observed_value = int(observed_match.group(1))
    cd_observed_unit = observed_match.group(2)
else:
    cd_observed_value = None
    cd_observed_unit = None


# Extract EPA Combined / City / Highway
epa_match = re.search(
    r"Combined/City/Highway:\s*(\d+)/(\d+)/(\d+)\s*(MPG|MPGe)",
    epa_section,
    re.IGNORECASE
)

if epa_match:
    epa_combined_value = int(epa_match.group(1))
    epa_city_value = int(epa_match.group(2))
    epa_highway_value = int(epa_match.group(3))
    epa_unit = epa_match.group(4)
else:
    epa_combined_value = None
    epa_city_value = None
    epa_highway_value = None
    epa_unit = None


print("C/D Observed:", cd_observed_value, cd_observed_unit)

print("EPA Combined/City/Highway:",
    epa_combined_value,
    epa_city_value,
    epa_highway_value,
    epa_unit
)

# Extract C/D 75-mph highway MPG
highway_match = re.search(
    r"75-mph Highway Driving:\s*(\d+)\s*mpg",
    cd_section
)

if highway_match:
    cd_highway_mpg = int(highway_match.group(1))
else:
    cd_highway_mpg = None


# Extract C/D 75-mph highway range
range_match = re.search(
    r"75-mph Highway Range:\s*(\d+)\s*miles",
    cd_section
)

if range_match:
    cd_highway_range_miles = int(range_match.group(1))
else:
    cd_highway_range_miles = None

print("C/D Highway MPG:", cd_highway_mpg)
print("C/D Highway Range:", cd_highway_range_miles)

# PHEV type Extraction case

phev_highway_match = re.search(
    r"75-mph Highway Driving,\s*EV/Hybrid Mode:\s*(\d+)\s*MPGe/(\d+)\s*mpg",
    cd_section,
    re.IGNORECASE
)

if phev_highway_match:
    cd_highway_ev_value = int(phev_highway_match.group(1))
    cd_highway_hybrid_value = int(phev_highway_match.group(2))
else:
    cd_highway_ev_value = None
    cd_highway_hybrid_value = None


phev_range_match = re.search(
    r"75-mph Highway Range,\s*EV/Hybrid Mode:\s*(\d+)/(\d+)\s*mi",
    cd_section,
    re.IGNORECASE
)

if phev_range_match:
    cd_highway_ev_range_miles = int(phev_range_match.group(1))
    cd_highway_hybrid_range_miles = int(phev_range_match.group(2))
else:
    cd_highway_ev_range_miles = None
    cd_highway_hybrid_range_miles = None

epa_mpge_match = re.search(
    r"Combined:\s*(\d+)\s*MPGe",
    epa_section,
    re.IGNORECASE
)

if epa_mpge_match:
    epa_combined_mpge = int(epa_mpge_match.group(1))
else:
    epa_combined_mpge = None

print("C/D Highway EV:", cd_highway_ev_value, "MPGe")
print("C/D Highway Hybrid:", cd_highway_hybrid_value, "MPG")
print("C/D EV Range:", cd_highway_ev_range_miles, "miles")
print("C/D Hybrid Range:", cd_highway_hybrid_range_miles, "miles")
print("EPA Combined MPGe:", epa_combined_mpge)

#Data pipeline structure 

fuel_data = extract_fuel_economy(cd_section, epa_section)

print("\n--- EXTRACTED DATA ---")

for key, value in fuel_data.items():
    print(key, "=", value)