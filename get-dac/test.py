import mcp4725_driver as mcp
dac = mcp.MCP4725(dynamic_range = 5.0, address = 0x61, verbose = False)
dac.set_number(4095) 