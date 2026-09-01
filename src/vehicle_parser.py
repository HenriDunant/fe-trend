import re


MAKES = [
    "Alfa Romeo",
    "Aston Martin",
    "Land Rover",
    "Mercedes-AMG",
    "Mercedes-Benz",
    "Rolls-Royce",

    "Acura",
    "Audi",
    "Bentley",
    "BMW",
    "Buick",
    "Cadillac",
    "Chevrolet",
    "Chrysler",
    "Dodge",
    "Ferrari",
    "Ford",
    "Genesis",
    "GMC",
    "Honda",
    "Hyundai",
    "Infiniti",
    "Jaguar",
    "Jeep",
    "Kia",
    "Lamborghini",
    "Lexus",
    "Lincoln",
    "Lucid",
    "Maserati",
    "Mazda",
    "McLaren",
    "Mini",
    "Mitsubishi",
    "Nissan",
    "Polestar",
    "Porsche",
    "Ram",
    "Rivian",
    "Subaru",
    "Tesla",
    "Toyota",
    "Volkswagen",
    "Volvo",
]


def extract_vehicle_identity(vehicle_name):

    data = {
        "make": None,
        "model_trim": None,
    }

    if not vehicle_name:
        return data

    # Remove model year from beginning
    name_without_year = re.sub(
        r"^\s*20\d{2}\s+",
        "",
        vehicle_name
    )

    # Finding manufacturer
    for make in sorted(MAKES, key=len, reverse=True):

        if name_without_year.lower().startswith(make.lower() + " "):
            data["make"] = make

            data["model_trim"] = name_without_year[
                len(make):
            ].strip()

            break

    return data