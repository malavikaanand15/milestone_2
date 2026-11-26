class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def water_plant(plant_name: str):
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def _run_watering_batch(plants: list[str], stop_on_error: bool) -> None:
    """Open the watering system-> water plants->always close in finally."""
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as err:
        print(f"Caught PlantError: {err}")
        if stop_on_error:
            print(".. ending tests and returning to main")
            return
    finally:
        print("Closing watering system")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    print("\nTesting valid plants...")
    _run_watering_batch(["Tomato", "Lettuce", "Carrots"], stop_on_error=False)

    print("\nTesting invalid plants...")
    _run_watering_batch(["Tomato", "lettuce", "Carrots"], stop_on_error=True)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
