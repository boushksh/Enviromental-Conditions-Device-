import time
import spidev

# MAX31865 register addresses
MAX31865_REG_CONFIG = 0x00
MAX31865_REG_TEMP = 0x01
MAX31865_REG_RTD_MSB = 0x01
MAX31865_REG_RTD_LSB = 0x02

# SPI bus and device
SPI_BUS = 0
SPI_DEVICE = 0

# Create SPI object
spi = spidev.SpiDev()
spi.open(SPI_BUS, SPI_DEVICE)
spi.max_speed_hz = 50000  # 50kHz clock speed for MAX31865
spi.mode = 0b00  # SPI mode 0 (CPOL=0, CPHA=0)

# Initialize MAX31865 (set up the configuration register)
def init_max31865():
    # Read the current configuration
    config = spi.xfer2([MAX31865_REG_CONFIG | 0x80, 0x00])[1]
    print(f"Initial Config Register: {config}")
    
    # Set configuration: Enable RTD, Disable 3-wire mode (if used), etc.
    # Enable 2-wire RTD (if you use a 2-wire configuration)
    config = 0xC2  # Example config to enable RTD and set appropriate settings
    
    # Write new configuration to the MAX31865
    spi.xfer2([MAX31865_REG_CONFIG, config])
    print(f"New Config Register Set: {config}")

# Read the temperature value from MAX31865
def read_temperature():
    # Read RTD MSB and LSB
    rtd_data = spi.xfer2([MAX31865_REG_RTD_MSB, 0x00, 0x00])
    rtd_msb = rtd_data[1]
    rtd_lsb = rtd_data[2]
    
    # Combine MSB and LSB to form the RTD value
    rtd_value = ((rtd_msb << 8) | rtd_lsb) >> 1  # Shift to remove the LSB bit
    
    # Calculate the temperature using the RTD value (this is a rough conversion)
    # Using the formula for PT100 RTD: T = (RTD - 32768) / 100
    # The value 32768 is based on the calibration of the MAX31865
    temperature = (rtd_value - 32768) / 100.0
    
    return temperature

def main():
    # Initialize the MAX31865
    init_max31865()
    
    # Read and print temperature every second
    try:
        while True:
            temperature = read_temperature()
            print(f"Temperature: {temperature:.2f} °C")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nProgram stopped.")
    finally:
        spi.close()

if __name__ == "__main__":
    main()
