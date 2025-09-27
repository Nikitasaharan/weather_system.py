class WeatherRecord:
    def __init__(self, date, city, temperature):
        self.date = date
        self.city = city
        self.temperature = temperature

class WeatherDataStorage:
    def __init__(self, years, cities):
        self.data = [[None for _ in range(len(cities))] for _ in range(len(years))]
        self.years = years
        self.cities = cities

    def populateArray(self, year_index, city_index, temp):
        self.data[year_index][city_index] = temp

    def rowMajorAccess(self):
        print("Row-Major Order:")
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                print(self.data[i][j], end=" ")
            print()

    def columnMajorAccess(self):
        print("Column-Major Order:")
        for j in range(len(self.data[0])):
            for i in range(len(self.data)):
                print(self.data[i][j], end=" ")
            print()

    def handleSparseData(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j] is None:
                    self.data[i][j] = -9999  # Sentinel value

    def retrieve(self, city, year):
        if year in self.years and city in self.cities:
            year_index = self.years.index(year)
            city_index = self.cities.index(city)
            return self.data[year_index][city_index]
        return None


# Example Usage
years = [2023, 2024]
cities = ["Delhi", "Mumbai"]
weather_system = WeatherDataStorage(years, cities)

weather_system.populateArray(0, 0, 32.5)  # Delhi 2023
weather_system.populateArray(0, 1, 28.3)  # Mumbai 2023
weather_system.populateArray(1, 0, 33.0)  # Delhi 2024

weather_system.handleSparseData()
weather_system.rowMajorAccess()
weather_system.columnMajorAccess()

print("Retrieve:", weather_system.retrieve("Mumbai", 2023))
