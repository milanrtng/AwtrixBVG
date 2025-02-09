import requests
import BvgAPI

AWTRIX_IP = "0.0.0.0"  # IP address of the AWTRIX clock

def bvg_app():
    url = f"http://{AWTRIX_IP}/api/custom"

    # JSON payload
    payload = {
        "text": BvgAPI.update_bvg_data(),  # Get the data from the BVG API
        "duration": 15,  # Duration for the display (in seconds)
        "icon": 2451,  # Icon to display
        "scrollSpeed": 50  # Speed at which the text scrolls
    }

    try:
        # Send HTTP POST request to the AWTRIX API
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("Sent successfully")
        else:
            print(f"Error: Status Code {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting: {e}")
