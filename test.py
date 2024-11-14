import gpsd

# Connect to the local gpsd
gpsd.connect()

# Get gps position
packet = gpsd.get_current()

# Get latitude and longitude
latitude, longitude = packet.position()
print(f"Latitude: {latitude}, Longitude: {longitude}")