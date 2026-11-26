def input_temperature(temp_str: str) -> int:
    temp: int = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    for value in ("25", "abc", "100", "-10"):
        print(f"\nInput data is '{value}'")
        try:
            test_temp = input_temperature(value)
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        else:
            print(f"Temperature is now {test_temp}°C")

    print("\nAll tests completed - program didn't crash!!")


if __name__ == "__main__":
    test_temperature()
