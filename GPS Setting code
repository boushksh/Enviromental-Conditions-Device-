import serial
import time

# Initialize UART communication (change the port name if necessary)
# '/dev/serial0' is typically used for UART communication on Raspberry Pi
gps_port = '/dev/serial0'
baud_rate = 9600  # Common baud rate for GPS modules

# Open serial connection to GPS module
gps = serial.Serial(gps_port, baud_rate, timeout=1)

def read_gps_data():
    while True:
        if gps.in_waiting > 0:
            # Read data from the GPS module
            gps_data = gps.readline().decode('ascii', errors='replace')
            
            if gps_data.startswith('$GPGGA'):
                print(f"GPS Data: {gps_data.strip()}")  # Print GPGGA data (time, latitude, longitude, etc.)
                # You can parse the GPGGA data further if needed for specific values

def main():
    print("Starting GPS communication...")
    try:
        read_gps_data()
    except KeyboardInterrupt:
        print("\nGPS reading stopped.")
    finally:
        gps.close()

if __name__ == '__main__':
    main()
