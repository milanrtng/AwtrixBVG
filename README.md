# BVG AWTRIX Integration

This script fetches BVG (Berlin Public Transport) departure information and displays it on your AWTRIX clock. It retrieves data from the [BVG API](https://v6.bvg.transport.rest/) and sends it to the AWTRIX via HTTP POST requests.

---

## Requirements

- **AWTRIX Clock**: Set up and connected to your local network. You'll need the clock's IP address.
- **BVG API Access**: The script uses the [BVG Transport REST API](https://v6.bvg.transport.rest/) to fetch data.

---


**Configure**:
- Set your **AWTRIX IP** in `app.py`:
  ```python
  AWTRIX_IP = "192.168.x.x"  # Replace with your AWTRIX clock's IP
  ```
- **BVG API URL**: The script uses the `BvgAPI.update_bvg_data()` function to retrieve BVG data. Make sure it works correctly with your desired parameters.
- Set the correct **Station ID** in the `BvgAPI` URL. Refer to the [BVG API documentation](https://v6.bvg.transport.rest/docs/) for details on how to find your station's `station_id`.

---
## Usage

Run the script: app.py

The script will send the BVG departure data to your AWTRIX clock.

---

## Notes

- **Personal Use Only**: This script is for private, non-commercial use only and is not affiliated with AWTRIX or BVG.
- **BVG API**: Check the [BVG API docs](https://v6.bvg.transport.rest/docs/) for further details on how to customize the data.

---

## Disclaimer

This script is provided "as-is" for personal use. The author is not responsible for any issues caused by its use.
