import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage, 'b-', linewidth=2)
    plt.title('Зависимость напряжения на выходе ЦАП от времени', fontsize=14)
    plt.xlabel('Время (с)', fontsize=12)
    plt.ylabel('Напряжение (В)', fontsize=12)
    plt.ylim(0, max_voltage * 1.05)
    if time:
        plt.xlim(min(time), max(time))
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
