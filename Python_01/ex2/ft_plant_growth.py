class Plant:
    def __init__(self, name: str, height: float, age_days: int):
        self.name = name
        self.height = height
        self.age_days = age_days

    def grow(self):
        self.height = round(self.height + 0.8, 1)

    def age(self):
        self.age_days += 1

    def display_status(self):
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")


def main():
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30)
    rose.display_status()
    initial_height = rose.height
    for day in range(1, 8):
        rose.grow()
        rose.age()
        print(f"=== Day {day} ===")
        rose.display_status()

    growth_week = round(rose.height - initial_height, 1)
    print(f"Growth this week: {growth_week}cm")


if __name__ == "__main__":
    main()
