class Plant:
    class _Stats:

        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, {self._show_calls} show"
            )

    def __init__(self, name: str, height: float, age_days: int) -> None:
        self.name = name
        self.height = float(height)
        self.age_days = int(age_days)
        self._stats = self._create_stats()

    def _create_stats(self) -> "_Stats":
        return Plant._Stats()

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return int(days) > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def grow(self, cm: float) -> None:
        self.height = round(self.height + float(cm), 1)
        self._stats.record_grow()

    def age(self, days: int) -> None:
        self.age_days += int(days)
        self._stats.record_age()

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age_days} days old")
        self._stats.record_show()

    def show_stats(self) -> None:
        self._stats.display()


class Flower(Plant):

    def __init__(
        self, name: str, height: float,
        age_days: int, color: str
    ) -> None:
        super().__init__(name, height, age_days)
        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Seed(Flower):

    def __init__(
        self,
        name: str,
        height: float,
        age_days: int,
        color: str,
        seed_count: int = 42,
    ) -> None:
        super().__init__(name, height, age_days, color)
        self._seed_yield = int(seed_count)
        self.seeds = 0

    def bloom(self) -> None:
        """Bloom the flower and populate its seeds."""
        super().bloom()
        self.seeds = self._seed_yield

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


class Tree(Plant):
    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls: int = 0

        def record_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_calls} shade")

    def __init__(
        self, name: str, height: float, age_days: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age_days)
        self.trunk_diameter = float(trunk_diameter)

    def _create_stats(self) -> "_TreeStats":
        return Tree._TreeStats()

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height}cm long and {self.trunk_diameter}cm wide."
        )
        stats: Tree._TreeStats = self._stats
        stats.record_shade()

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age_days: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, age_days)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, cm: float) -> None:
        super().grow(cm)

    def age(self, days: int) -> None:
        super().age(days)
        self.nutritional_value += int(days)

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


def display_plant_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.show_stats()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_plant_statistics(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_statistics(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow", seed_count=42)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_plant_statistics(sunflower)

    print("\n=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    display_plant_statistics(unknown)


if __name__ == "__main__":
    main()
