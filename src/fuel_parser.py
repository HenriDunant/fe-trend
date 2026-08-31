import re


def extract_fuel_economy(cd_section, epa_section):

    data = {
        "cd_observed_value": None,
        "cd_observed_unit": None,

        "cd_highway_mpg": None,
        "cd_highway_range_miles": None,

        "cd_highway_ev_mpge": None,
        "cd_highway_hybrid_mpg": None,
        "cd_highway_ev_range_miles": None,
        "cd_highway_hybrid_range_miles": None,

        "epa_combined_mpg": None,
        "epa_city_mpg": None,
        "epa_highway_mpg": None,

        "epa_combined_mpge": None,
        "epa_city_mpge": None,
        "epa_highway_mpge": None,
    }

    # C/D observed MPG or MPGe
    match = re.search(
        r"Observed:\s*(\d+)\s*(MPGe?)\b",
        cd_section,
        re.IGNORECASE,
    )

    if match:
        data["cd_observed_value"] = int(match.group(1))

        if match.group(2).lower() == "mpge":
            data["cd_observed_unit"] = "MPGe"
        else:
            data["cd_observed_unit"] = "MPG"

    # Normal C/D 75-mph highway MPG
    match = re.search(
        r"75-mph Highway Driving:\s*(\d+)\s*mpg\b",
        cd_section,
        re.IGNORECASE,
    )

    if match:
        data["cd_highway_mpg"] = int(match.group(1))

    # Normal C/D highway range
    match = re.search(
        r"75-mph Highway Range:\s*(\d+)\s*(?:mi|miles)\b",
        cd_section,
        re.IGNORECASE,
    )

    if match:
        data["cd_highway_range_miles"] = int(match.group(1))

    # PHEV C/D highway EV / Hybrid mode
    match = re.search(
        r"75-mph Highway Driving,\s*EV/Hybrid Mode:\s*"
        r"(\d+)\s*MPGe/(\d+)\s*mpg\b",
        cd_section,
        re.IGNORECASE,
    )

    if match:
        data["cd_highway_ev_mpge"] = int(match.group(1))
        data["cd_highway_hybrid_mpg"] = int(match.group(2))

    # PHEV C/D highway range EV / Hybrid mode
    match = re.search(
        r"75-mph Highway Range,\s*EV/Hybrid Mode:\s*"
        r"(\d+)/(\d+)\s*mi\b",
        cd_section,
        re.IGNORECASE,
    )

    if match:
        data["cd_highway_ev_range_miles"] = int(match.group(1))
        data["cd_highway_hybrid_range_miles"] = int(match.group(2))

    # EPA gasoline MPG
    match = re.search(
        r"Combined/City/Highway:\s*"
        r"(\d+)/(\d+)/(\d+)\s*mpg\b",
        epa_section,
        re.IGNORECASE,
    )

    if match:
        data["epa_combined_mpg"] = int(match.group(1))
        data["epa_city_mpg"] = int(match.group(2))
        data["epa_highway_mpg"] = int(match.group(3))

    # EPA EV MPGe
    match = re.search(
        r"Combined/City/Highway:\s*"
        r"(\d+)/(\d+)/(\d+)\s*MPGe\b",
        epa_section,
        re.IGNORECASE,
    )

    if match:
        data["epa_combined_mpge"] = int(match.group(1))
        data["epa_city_mpge"] = int(match.group(2))
        data["epa_highway_mpge"] = int(match.group(3))

    # EPA PHEV combined MPGe
    match = re.search(
        r"Combined(?:\s+Gasoline\s*\+\s*Electricity)?:\s*"
        r"(\d+)\s*MPGe\b",
        epa_section,
        re.IGNORECASE,
    )

    if match:
        data["epa_combined_mpge"] = int(match.group(1))

    return data