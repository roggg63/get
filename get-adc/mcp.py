import time
from mcp3021_driver import MCP3021
from adc_plot import plot_voltage_vs_time, plot_sampling_period_hist

def main():
    DYNAMIC_RANGE = 5.0
    DURATION = 3.0

    voltage_values = []
    time_values = []

    try:
        adc = MCP3021(dynamic_range=DYNAMIC_RANGE, verbose=False)

        start_time = time.time()
        print(f"Измеряем напряжение через MCP3021 в течение {DURATION} секунд...")

        while time.time() - start_time < DURATION:
            v = adc.get_voltage()
            t = time.time() - start_time
            voltage_values.append(v)
            time_values.append(t)

        print("Измерения завершены.")
        print("Строим график напряжения от времени...")
        plot_voltage_vs_time(time_values, voltage_values, DYNAMIC_RANGE)

        print("Строим гистограмму длительности измерений...")
        plot_sampling_period_hist(time_values)

    except KeyboardInterrupt:
        print("\nПрерывание пользователем")

    finally:
        if 'adc' in locals():
            adc.deinit()

if __name__ == "__main__":
    main()
