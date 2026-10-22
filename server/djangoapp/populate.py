from .models import CarMake, CarModel


def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology", "country": "Japan"},
        {"name": "Mercedes", "description": "Great cars. German technology", "country": "Germany"},
        {"name": "Audi", "description": "Great cars. German technology", "country": "Germany"},
        {"name": "Kia", "description": "Great cars. Korean technology", "country": "South Korea"},
        {"name": "Toyota", "description": "Great cars. Japanese technology", "country": "Japan"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(
            name=data['name'],
            description=data['description'],
            country=data['country'],
        ))

    # (index into car_make_instances, model name, type, year)
    car_model_data = [
        (0, "Pathfinder", "SUV", 2023),
        (0, "Qashqai", "SUV", 2023),
        (0, "XTRAIL", "SUV", 2023),
        (1, "A-Class", "SUV", 2023),
        (1, "C-Class", "SUV", 2023),
        (1, "E-Class", "SUV", 2023),
        (2, "A4", "Sedan", 2023),
        (2, "A5", "Sedan", 2023),
        (2, "A6", "Sedan", 2023),
        (3, "Sorrento", "SUV", 2023),
        (3, "Carnival", "SUV", 2023),
        (3, "Cerato", "Sedan", 2023),
        (4, "Corolla", "Sedan", 2023),
        (4, "Camry", "Sedan", 2023),
        (4, "Kluger", "SUV", 2023),
    ]

    for make_index, name, car_type, year in car_model_data:
        CarModel.objects.create(
            car_make=car_make_instances[make_index],
            name=name,
            type=car_type,
            year=year,
        )
