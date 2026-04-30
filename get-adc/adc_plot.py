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

def plot_sampling_period_hist(time):
    if len(time) < 2:
        print("Недостаточно данных для построения гистограммы")
        return
        
    sampling_periods = [time[i] - time[i-1] for i in range(1, len(time))]

    plt.figure(figsize=(10, 6))
    plt.hist(sampling_periods, bins=30, color='green', edgecolor='black', alpha=0.7)
    plt.title('Распределение длительности измерений', fontsize=14)
    plt.xlabel('Время измерения (с)', fontsize=12)
    plt.ylabel('Количество измерений', fontsize=12)
    plt.xlim(0, 0.06)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
