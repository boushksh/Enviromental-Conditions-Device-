import time
import smbus2

# I2C address for LSM303AGR (it may vary, typically it's 0x1D)
LSM303AGR_ADDR = 0x1D

# Register addresses for accelerometer (ACC) and magnetometer (MAG)
ACC_CTRL_REG1_A = 0x20
MAG_CTRL_REG1_M = 0x20
ACC_OUT_X_L_A = 0x28  # Accelerometer output X-axis low byte
MAG_OUT_X_L_M = 0x03  # Magnetometer output X-axis low byte

# Create an I2C bus object
bus = smbus2.SMBus(1)  # Use I2C bus 1 (for Raspberry Pi)

# Function to initialize the LSM303AGR accelerometer and magnetometer
def init_lsm303agr():
    # Accelerometer: enable all axes (X, Y, Z), and set output data rate
    bus.write_byte_data(LSM303AGR_ADDR, ACC_CTRL_REG1_A, 0x57)  # 0x57 for normal mode, ODR = 100 Hz
    # Magnetometer: enable the sensor with default settings
    bus.write_byte_data(LSM303AGR_ADDR, MAG_CTRL_REG1_M, 0x70)  # 0x70 for normal mode, 10 Hz

# Function to read 2 bytes of data from the specified register (for both ACC and MAG)
def read_word_data(address, register):
    low_byte = bus.read_byte_data(address, register)
    high_byte = bus.read_byte_data(address, register + 1)
    return (high_byte << 8) + low_byte

# Function to read accelerometer data (X, Y, Z axes)
def read_accelerometer():
    acc_x = read_word_data(LSM303AGR_ADDR, ACC_OUT_X_L_A)
    acc_y = read_word_data(LSM303AGR_ADDR, ACC_OUT_X_L_A + 2)
    acc_z = read_word_data(LSM303AGR_ADDR, ACC_OUT_X_L_A + 4)

    # Convert to signed 16-bit values
    if acc_x > 32767:
        acc_x -= 65536
    if acc_y > 32767:
        acc_y -= 65536
    if acc_z > 32767:
        acc_z -= 65536

    return acc_x, acc_y, acc_z

# Function to read magnetometer data (X, Y, Z axes)
def read_magnetometer():
    mag_x = read_word_data(LSM303AGR_ADDR, MAG_OUT_X_L_M)
    mag_y = read_word_data(LSM303AGR_ADDR, MAG_OUT_X_L_M + 2)
    mag_z = read_word_data(LSM303AGR_ADDR, MAG_OUT_X_L_M + 4)

    # Convert to signed 16-bit values
    if mag_x > 32767:
        mag_x -= 65536
    if mag_y > 32767:
        mag_y -= 65536
    if mag_z > 32767:
        mag_z -= 65536

    return mag_x, mag_y, mag_z

def main():
    # Initialize the LSM303AGR sensor
    init_lsm303agr()
    print("LSM303AGR Initialized")

    try:
        while True:
            # Read accelerometer and magnetometer data
            acc_x, acc_y, acc_z = read_accelerometer()
            mag_x, mag_y, mag_z = read_magnetometer()

            # Print the accelerometer data
            print(f"Accelerometer Data: X={acc_x}, Y={acc_y}, Z={acc_z}")

            # Print the magnetometer data
            print(f"Magnetometer Data: X={mag_x}, Y={mag_y}, Z={mag_z}")

            # Wait for 1 second before reading again
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nProgram stopped.")
    finally:
        bus.close()

if __name__ == '__main__':
    main()
