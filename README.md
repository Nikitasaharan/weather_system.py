# Weather Data Storage System

## Description
A Weather Data Storage System designed to systematically collect, store, and manage weather-related data such as temperature, humidity, and atmospheric conditions using 2D arrays and Abstract Data Types (ADTs). This project demonstrates the ability to handle both complete and sparse datasets efficiently.

## Features
- Weather Record ADT
- Year-wise and city-wise temperature data storage
- Row-major and column-major access methods
- Sparse data handling using sentinel values
- Time and space complexity analysis

## Usage
1. Clone the repository  
2. Run the Python script  
3. Populate the array and test different access methods  
4. Retrieve data based on city and year

## Example
```python
years = [2023, 2024]
cities = ["Delhi", "Mumbai"]
weather_system = WeatherDataStorage(years, cities)

weather_system.populateArray(0, 0, 32.5)
weather_system.populateArray(0, 1, 28.3)
weather_system.populateArray(1, 0, 33.0)

weather_system.handleSparseData()
weather_system.rowMajorAccess()
weather_system.columnMajorAccess()

print(weather_system.retrieve("Mumbai", 2023))


## Example
