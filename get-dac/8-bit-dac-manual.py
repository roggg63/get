import RPi.GPIO as GPIO

dynamic_range = 3.3

leds = [24, 22, 23, 27, 17, 25, 12, 16]

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} B)")
        print("Устанавливаем 0.0 В")
        return 0

    return int(voltage / dynamic_range * 255)

def number_to_dac(number):

    bits = bin(number)[2:].zfill(8)
    for i, bit in enumerate(bits):
        GPIO.output(leds[i], int(bit))



GPIO.setmode(GPIO.BCM)



GPIO.setup(leds, GPIO.OUT)


try:
    while True:
        try:
            voltage = float(input("Введите напряжение в вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз\n")

finally:
    GPIO.output(leds, 0)
    GPIO.cleanup

