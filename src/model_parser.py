import csv
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]

REFERENCE_FILE = (
    PROJECT_ROOT
    / "data"
    / "reference"
    / "vehicle_models.csv"
)


def load_model_reference():

    models = {}

    with open(
        REFERENCE_FILE,
        newline="",
        encoding="utf-8-sig"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            make = row["make"].strip()
            model = row["model"].strip()

            models.setdefault(
                make.lower(),
                []
            ).append(model)

    # Longest model names checked first
    for make in models:
        models[make].sort(
            key=len,
            reverse=True
        )

    return models


def extract_model_trim(
    make,
    model_trim,
    model_reference
):

    data = {
        "model": None,
        "trim": None,
    }

    if not make or not model_trim:
        return data

    possible_models = model_reference.get(
        make.lower(),
        []
    )

    for model in possible_models:

        if model_trim.lower() == model.lower():
            data["model"] = model
            return data

        prefix = model.lower() + " "

        if model_trim.lower().startswith(prefix):

            data["model"] = model

            data["trim"] = model_trim[
                len(model):
            ].strip()

            return data

    return data