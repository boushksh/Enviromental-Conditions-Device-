import csv
import time
from temperature_sensor_setting_code import read_temperature
from gps_setting_code import read_gps
from accelerometer_magnetic_field_sensor_setting_code import read_accelerometer, read_magnetometer

# CSV File Setup
csv_filename = "sensor_data.csv"
fieldnames = ['Timestamp', 'Latitude', 'Longitude', 'Altitude', 'Speed', 'Temperature', 'Acceleration (X)', 'Acceleration (Y)', 'Acceleration (Z)', 'Magnetic Field (X)', 'Magnetic Field (Y)', 'Magnetic Field (Z)']

# Initialize CSV file (create and write headers if file doesn't exist)
try:
    with open(csv_filename, mode='x', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
except FileExistsError:
    pass  # If the file already exists, don't write the header again

def append_data_to_csv(data):
    """ Append the sensor data to the CSV file. """
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(data)

def run_sensors():
    while True:
        # Read data from the sensors
        gps_data = read_gps()  # This should return a tuple (latitude, longitude, altitude, speed)
        temperature_data = read_temperature()  # This should return temperature in Celsius
        accelerometer_data = read_accelerometer()  # This should return (x, y, z) acceleration data
        magnetometer_data = read_magnetometer()  # This should return (x, y, z) magnetic field data

        # Get the current timestamp
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

        # Prepare the data for the CSV
        data = {
            'Timestamp': timestamp,
            'Latitude': gps_data[0],
            'Longitude': gps_data[1],
            'Altitude': gps_data[2],
            'Speed': gps_data[3],
            'Temperature': temperature_data,
            'Acceleration (X)': accelerometer_data[0],
            'Acceleration (Y)': accelerometer_data[1],
            'Acceleration (Z)': accelerometer_data[2],
            'Magnetic Field (X)': magnetometer_data[0],
            'Magnetic Field (Y)': magnetometer_data[1],
            'Magnetic Field (Z)': magnetometer_data[2]
