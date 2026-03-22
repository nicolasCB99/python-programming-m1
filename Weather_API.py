import requests

# Function to get weather data
def get_weather():

    # Coordinates for Freeport, NY
    latitude = 40.6576
    longitude = -73.5832

    # An updated URL for Fahrenheit and mph
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&temperature_unit=fahrenheit&windspeed_unit=mph"

    try:
        # Send a request to the API
        response = requests.get(url, timeout=10)

        # Check if the request was successful
        response.raise_for_status()

        # Convert response to JSON
        data = response.json()

        # Extract the current weather data in Freeport
        current = data.get("current_weather", {})

        temperature = current.get("temperature")
        windspeed = current.get("windspeed")
        winddirection = current.get("winddirection")

        # Display it in a clean output
        print("=== Current Weather in Freeport, NY ===")
        print(f"Temperature: {temperature}°F")
        print(f"Wind Speed: {windspeed} mph")
        print(f"Wind Direction: {winddirection}°")

    except requests.exceptions.RequestException:
        print("Error: Unable to retrieve weather data.")


# The Main function
def main():

    print("Weather Program")
    get_weather()


if __name__ == "__main__":
    main()