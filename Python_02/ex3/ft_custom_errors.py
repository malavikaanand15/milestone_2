class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant_health(is_wilting: bool) -> None:
    if is_wilting:
        raise PlantError("The tomato plant is wilting!")


def check_water_supply(ltr_current: float, ltr_need: float) -> None:
    if ltr_current < ltr_need:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors ===")

    print("\nTesting PlantError:")
    try:
        check_plant_health(True)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError:")
    try:
        check_water_supply(2.0, 10.0)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        check_plant_health(True)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
    try:
        check_water_supply(2.0, 10.0)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
