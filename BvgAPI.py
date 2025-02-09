import requests
from datetime import datetime, timezone

# Manually configurable station ID
station_id = "900181001"  # Change this to the desired station ID

def update_bvg_data():
    try:
        # Dynamic URL with the manually configurable station_id
        url = f"https://v6.bvg.transport.rest/stops/{station_id}/departures?tram=true&duration=60&results=10&pretty=true"
        print(f"Sending request to BVG API for station {station_id}...")
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        print("Data received from API.")
        now = datetime.now(timezone.utc)
        print(f"Current time (UTC): {now}")

        valid_end_stations = {
            "falkenberg", "betriebshof lichtenberg", "johannisthal, haeckelstr.",
            "s adlershof", "bahnhofstr./lindenstr.", "s schöneweide"
        }

        print(f"Valid end stations: {valid_end_stations}")

        # Filter the departures to include only those going to valid end stations
        departures = [
            dep for dep in data.get("departures", [])
            if dep.get("direction", "").lower() in valid_end_stations
        ]
        print(f"Filtered departures: {departures}")

        # Sort the departures by time
        departures.sort(key=lambda d: datetime.fromisoformat(d.get("when").replace("Z", "+00:00")))
        print(f"Sorted departures: {departures}")

        # Find the first departure that is more than 5 minutes away
        valid_departures = []  # List to hold future departures

        for departure in departures:
            when = departure.get("when")
            line = departure.get("line", {}).get("name")
            if when and line:
                departure_time = datetime.fromisoformat(when.replace("Z", "+00:00"))
                time_difference = (departure_time - now).total_seconds() / 60
                rounded_time_difference = round(time_difference)  # Round to the nearest minute

                if rounded_time_difference < 0:
                    print(f"Skipping departure {line} at {departure_time} because it's already in the past.")
                    continue  # Skip past departures

                print(f"Checking departure {line} at {departure_time}, which is {rounded_time_difference} minutes away.")

                # Add only future departures that are more than 5 minutes away
                if rounded_time_difference > 5:
                    valid_departures.append((line, rounded_time_difference))

        # Check if we found valid future departures
        if valid_departures:
            # Return the first valid departure
            line, time_left = valid_departures[0]
            print(f"Found valid departure: {line} in {time_left} min")
            return f"{line} in {time_left} min"

        print("No valid departures found within the next 5 minutes.")
        return "Error: No valid departures found"

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return f"Error: {e}"
    except Exception as e:
        print(f"Unexpected error: {e}")
        return f"Error: {e}"
