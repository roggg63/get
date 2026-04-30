import time
from r2r_adc import R2R_ADC
from adc_plot import plot_voltage_vs_time

def main():
    DYNAMIC_RANGE = 3.30
    DURATION = 3.0
    COMPARE_TIME = 0.0001

    voltage_values = []
    time_values = []

    try:
        adc = R2R_ADC(dynamic_range=DYNAMIC_RANGE,
                      compare_time=COMPARE_TIME,
                      verbose=False)

        start_time = time.time()
        print(f"Измеряем напряжение в течение {DURATION} секунд...")

        while time.time() - start_time < DURATION:
            v = adc.get_sc_voltage()
            t = time.time() - start_time
            voltage_values.append(v)
            time_values.append(t)

        print("Измерения завершены. Построение графика...")
        plot_voltage_vs_time(time_values, voltage_values, DYNAMIC_RANGE)

    except KeyboardInterrupt:
        print("\nПрерывание пользователем")

    finally:
        if 'adc' in locals():
            adc.cleanup()

if __name__ == "__main__":
    main()
