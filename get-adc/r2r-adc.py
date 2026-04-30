
import RPi.GPIO as GPIO
import time

class R2R_ADC:

    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time


        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def number_to_dac(self, number):
        
        if self.verbose:
            print(f"Подача числа {number} на ЦАП")
        for i, pin in enumerate(self.bits_gpio):
            bit = (number >> i) & 1
            GPIO.output(pin, bit)

    def sequential_counting_adc(self):
        for code in range(256):
            self.number_to_dac(code)
            time.sleep(self.compare_time)

            if GPIO.input(self.comp_gpio) == 1:
                if self.verbose:
                    print(f"Превышение достигнуто при коде {code}")
                return code

        if self.verbose:
            print("Превышения не достигнуто, вернём 255")
        return 255

    def get_sc_voltage(self):
        code = self.sequential_counting_adc()
        voltage = code * self.dynamic_range / 255.0
        if self.verbose:
            print(f"Измеренный код: {code}, напряжение: {voltage:.3f} В")
        return voltage

    def cleanup(self):

        self.number_to_dac(0)
        GPIO.cleanup(self.bits_gpio + [self.comp_gpio])
        if self.verbose:
            print("GPIO очищены")

    def __del__(self):
        self.cleanup()


if __name__ == "__main__":
    DYNAMIC_RANGE = 3.30

    try:
        adc = R2R_ADC(dynamic_range=DYNAMIC_RANGE, compare_time=0.01, verbose=False)

        print("Начинаем измерение напряжения. Для выхода нажмите Ctrl+C\n")

        while True:
            voltage = adc.get_sc_voltage()
            print(f"Напряжение: {voltage:.3f} В")
            time.sleep(0.05)

    except KeyboardInterrupt:
        print("\nПрерывание по запросу пользователя")

    finally:
        if 'adc' in locals():
            adc.cleanup()
