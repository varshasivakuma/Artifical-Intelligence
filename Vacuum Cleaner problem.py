class VacuumCleaner:
    def __init__(self):
        self.location_A = "dirty"
        self.location_B = "dirty"
        self.current_location = "A"

    def clean(self, location):
        if location == "A":
            self.location_A = "clean"
        elif location == "B":
            self.location_B = "clean"

    def move(self, new_location):
        self.current_location = new_location

    def is_dirty(self, location):
        if location == "A":
            return self.location_A == "dirty"
        elif location == "B":
            return self.location_B == "dirty"

    def run(self):
        print("Initial State:")
        print(f"Location A: {self.location_A}")
        print(f"Location B: {self.location_B}")

        while self.is_dirty("A") or self.is_dirty("B"):
            if self.current_location == "A":
                if self.is_dirty("A"):
                    self.clean("A")
                    print("Cleaning at location A")
                self.move("B")
                print("Moving to location B")
            else:
                if self.is_dirty("B"):
                    self.clean("B")
                    print("Cleaning at location B")
                self.move("A")
                print("Moving to location A")

        print("Final State:")
        print(f"Location A: {self.location_A}")
        print(f"Location B: {self.location_B}")
        print("Cleaning complete.")

if __name__ == "__main__":
    vacuum = VacuumCleaner()
    vacuum.run()
