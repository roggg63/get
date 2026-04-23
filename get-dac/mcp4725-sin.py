import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 4.8
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = mcp.MCP4725(dynamic_range=5.0, address=0x61, verbose=False)
    while True:
        t = time.time()
        norm = sg.get_sin_wave_amplitude(signal_frequency, t)
        voltage = norm * amplitude
        dac.set_voltage(voltage)
        sg.wait_for_sampling_period(sampling_frequency)
finally:
    dac.deinit()
