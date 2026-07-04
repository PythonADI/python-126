import random
import datetime
import time
import json


class TemperatureRecord:
    def __init__(self, value, dt):
        self.value = value
        self.datetime = dt


class Thermometer:
    def __init__(self, name):
        self.name = name
        self.history = []

    def current_temperature(self):
        # imitation of getting data from actual device
        current_temperature = random.randint(15, 30)

        self.history.append(TemperatureRecord(current_temperature, datetime.datetime.now()))

        return current_temperature
    
    def show_history(self):
        print(f"\n--- {self.name} ---")
        for record in self.history:
            print(f"{record.value} - {record.datetime}")
        
    def export_data(self, file_name):
        with open(file_name, "w") as f:
            json.dump([
                {
                    "value": record.value,
                    "datetime": record.datetime.isoformat()
                } for record in self.history
            ], f, indent=4)

    def import_data(self, file_name):
        try:
            with open(file_name, "r") as f:
                self.history = [
                    TemperatureRecord(
                        record["value"], 
                        datetime.datetime.fromisoformat(record["datetime"])
                    )
                    for record in json.load(f)
                ]
        except FileNotFoundError:
            print("WARNING Could not find file you proivded")


# imperative code
dev1 = Thermometer("Storage")
dev1.import_data(f"{dev1.name}.json")

dev2 = Thermometer("Room 1")

for _ in range(10):
    dev1.current_temperature()

print(dev2.current_temperature())


dev1.show_history()
dev2.show_history()

dev1.export_data(f"{dev1.name}.json")


