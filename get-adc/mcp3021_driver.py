import smbus
import time

class MCP3021:
    def __init__(self, dynamic_range, verbose=False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose

    def deinit(self):
        self.bus.close()

    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)

        if self.verbose:
            print(f"Принятые данные: {data}, "
                  f"Старший байт: {upper_data_byte:02x}, "
                  f"Младший байт: {lower_data_byte:02x}, "
                  f"Число: {number}")

        return number

    def get_voltage(self):
        code = self.get_number()
        voltage = code * self.dynamic_range / 1023.0
        if self.verbose:
            print(f"Код: {code}, напряжение: {voltage:.3f} В")
        return voltage


if __name__ == "__main__":
    DYNAMIC_RANGE = 5.0
    try:
        adc = MCP3021(dynamic_range=DYNAMIC_RANGE, verbose=False)
        print("Начинаем измерение напряжения через MCP3021 (I2C).")
        print("Для выхода нажмите Ctrl+C\n")

        while True:
            v = adc.get_voltage()
            print(f"Напряжение: {v:.3f} В")
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nПрерывание пользователем")

    finally:
        if 'adc' in locals():
            adc.deinit()
