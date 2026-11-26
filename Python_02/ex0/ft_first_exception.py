def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    for value in ("25", "abc"):
        print(f"\nInput data is '{value}'")
        try:
            test_temp: int = input_temperature(value)
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")
        else:
            print(f"Temperature is now {test_temp}°C")

    print("\nAll tests completed - program didn't crash!!")


if __name__ == "__main__":
    test_temperature()
