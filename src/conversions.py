def mpg_to_l_per_100km(mpg):
    if mpg is None or mpg <= 0:
        return None

    return round(235.215 / mpg, 2)


def mpge_to_kwh_per_100km(mpge):
    if mpge is None or mpge <= 0:
        return None

    return round(2094.4 / mpge, 2)


def miles_to_km(miles):
    if miles is None:
        return None

    return round(miles * 1.609344, 1)


def add_metric_conversions(record):

    metric = {}

    # C/D observed
    metric["cd_observed_l_per_100km"] = None
    metric["cd_observed_kwh_per_100km"] = None

    if record["cd_observed_unit"] == "MPG":
        metric["cd_observed_l_per_100km"] = mpg_to_l_per_100km(
            record["cd_observed_value"]
        )

    elif record["cd_observed_unit"] == "MPGe":
        metric["cd_observed_kwh_per_100km"] = mpge_to_kwh_per_100km(
            record["cd_observed_value"]
        )

    # C/D highway
    metric["cd_highway_l_per_100km"] = mpg_to_l_per_100km(
        record["cd_highway_mpg"]
    )

    metric["cd_highway_ev_kwh_per_100km"] = mpge_to_kwh_per_100km(
        record["cd_highway_ev_mpge"]
    )

    metric["cd_highway_hybrid_l_per_100km"] = mpg_to_l_per_100km(
        record["cd_highway_hybrid_mpg"]
    )

    # EPA MPG
    metric["epa_combined_l_per_100km"] = mpg_to_l_per_100km(
        record["epa_combined_mpg"]
    )

    metric["epa_city_l_per_100km"] = mpg_to_l_per_100km(
        record["epa_city_mpg"]
    )

    metric["epa_highway_l_per_100km"] = mpg_to_l_per_100km(
        record["epa_highway_mpg"]
    )

    # EPA MPGe
    metric["epa_combined_kwh_per_100km"] = mpge_to_kwh_per_100km(
        record["epa_combined_mpge"]
    )

    metric["epa_city_kwh_per_100km"] = mpge_to_kwh_per_100km(
        record["epa_city_mpge"]
    )

    metric["epa_highway_kwh_per_100km"] = mpge_to_kwh_per_100km(
        record["epa_highway_mpge"]
    )

    # Range
    metric["cd_highway_range_km"] = miles_to_km(
        record["cd_highway_range_miles"]
    )

    metric["cd_highway_ev_range_km"] = miles_to_km(
        record["cd_highway_ev_range_miles"]
    )

    metric["cd_highway_hybrid_range_km"] = miles_to_km(
        record["cd_highway_hybrid_range_miles"]
    )

    return metric