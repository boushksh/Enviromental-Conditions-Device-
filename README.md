# Airmo-Task-
Test task for Hardware Engineer

# Raspberry Pi Sensor Interface: GPS, Temperature, Accelerometer, and Magnetometer

This project demonstrates interfacing **PA1616S GPS**, **MAX31865 PT100 amplifier**, and **LSM303AGR accelerometer/magnetometer** with a **Raspberry Pi** using UART, SPI, and I2C communication protocols.

## Hardware Setup

### Raspberry Pi GPIO Pinout
- **I2C (LSM303AGR)**:  
  - SDA → **GPIO 2 (Pin 3)**  
  - SCL → **GPIO 3 (Pin 5)**

- **SPI (MAX31865)**:  
  - MOSI → **GPIO 10 (Pin 19)**  
  - MISO → **GPIO 9 (Pin 21)**  
  - SCK → **GPIO 11 (Pin 23)**  
  - CS → **GPIO 8 (Pin 24)**

- **UART (PA1616S GPS)**:  
  - TX → **GPIO 14 (Pin 8)**  
  - RX → **GPIO 15 (Pin 10)**

## Software Setup

### Dependencies
1. Install libraries:
   ```bash
   sudo apt-get update
   sudo apt-get install python3-smbus python3-spidev python3-serial
   ```

### Code Files
- **Temperature Sensor Setting Code**: Reads data from **MAX31865 PT100 amplifier** (SPI).
- **GPS Setting Code**: Reads data from **PA1616S GPS module** (UART).
- **Accelerometer & Magnetic Field Sensor Setting Code**: Reads data from **LSM303AGR accelerometer/magnetometer** (I2C).

### Running the Scripts
1. Enable **I2C, SPI, UART** using `sudo raspi-config`.
2. Run the scripts:
   ```bash
   python3 temperature_sensor_setting_code.py
   python3 gps_setting_code.py
   python3 accelerometer_magnetic_field_sensor_setting_code.py
   ```

## Sensor Data
- **GPS Module**: Latitude, Longitude, Altitude (m), Speed (km/h).
- **MAX31865 PT100**: Temperature (°C).
- **LSM303AGR**: Acceleration (g) and Magnetic Field (Gauss).
