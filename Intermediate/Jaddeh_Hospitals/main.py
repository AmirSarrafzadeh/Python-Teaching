import requests
import pandas as pd
import xml.etree.ElementTree as ET
pd.set_option('display.width', None)
from geopy.geocoders import Nominatim
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Define the Overpass API URL
api_url = r"https://overpass-api.de/api/interpreter"
Jaddeh_box = (21.47351753334985, 38.99940490722656, 21.68933332636862, 39.52880859375)
hospital = "hospital"

# Define the request body
request_body = f'node [amenity={hospital}] {Jaddeh_box}; out;'

# Send the POST request
response = requests.post(api_url, data=request_body)
xml_data = response.content.decode("utf-8")

# Parse the XML data
root = ET.fromstring(xml_data)

# Initialize lists to store data
ids = []
lats = []
longs = []
amenities = []
names = []
capacities = []
emergencies = []
opening_hours = []
phones = []
websites = []
emails = []
twitters = []

# Extract data from XML
for node in root.findall('node'):
    ids.append(node.attrib.get('id'))
    lats.append(node.attrib.get('lat'))
    longs.append(node.attrib.get('lon'))
    amenity = None
    name = None
    capacity = None
    emergency = None
    opening_hour = None
    phone = None
    website = None
    email = None
    twitter = None

    for tag in node.findall('tag'):
        if tag.attrib.get('k') == 'amenity':
            amenity = tag.attrib.get('v')
        elif tag.attrib.get('k') == 'name:en':
            name = tag.attrib.get('v')
        elif tag.attrib.get('k') == 'emergency':
            emergency = tag.attrib.get('v')
        elif tag.attrib.get('k') == 'capacity':
            capacity = tag.attrib.get('v')
        elif tag.attrib.get('k') == 'opening_hours':
            opening_hour = tag.attrib.get('v')
        elif tag.attrib.get('k') == 'phone':
            phone = tag.attrib.get('v')
        elif tag.attrib.get('k') == 'website':
            website = tag.attrib.get('v')
        elif tag.attrib.get('k') == 'name':
            name = tag.attrib.get('v')
        elif tag.attrib.get('k') == 'email':
            email = tag.attrib.get('v')
        elif tag.attrib.get('k') == 'twitter':
            twitter = tag.attrib.get('v')

    amenities.append(amenity)
    names.append(name)
    capacities.append(capacity)
    emergencies.append(emergency)
    opening_hours.append(opening_hour)
    phones.append(phone)
    websites.append(website)
    emails.append(email)
    twitters.append(twitter)

# Create DataFrame
data = {
    'id': ids,
    'lat': lats,
    'lon': longs,
    'amenity': amenities,
    'name': names,
    'capacity': capacities,
    'emergency': emergencies,
    'opening_hours': opening_hours,
    'phone': phones,
    'website': websites,
    'email': emails,
    'twitter': twitters
}

# Create DataFrame
df = pd.DataFrame(data)

# Initialize geocoder
geolocator = Nominatim(user_agent="my_app")

# Define a function to get address from latitude and longitude
def get_address(row):
    location = geolocator.reverse((row['lat'], row['lon']))
    return location.address if location else None

# Apply the get_address function to the DataFrame
df['address'] = df.apply(get_address, axis=1)


# Save DataFrame to CSV with UTF-8 encoding
df.to_csv('Saudi_Arabia.csv', encoding='utf-8', index=False)