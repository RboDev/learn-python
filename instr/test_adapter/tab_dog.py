"""Specific high level driver for a DUT of type B.

The Type A DUT:
  - requires a DC Voltage power supply of 3.0V an 1.8V
  - has an ENABLE pin to wake up the chip
  - has a reset pin

"""

from .tab import TAB

REG_3V3 = (1, 3.0)
REG_1V8 = (2, 1.8)

PIO_ENABLE = 3
PIO_RESET = 2

class TabDog:
    """Test Adapter Driver for Dog DUTs."""

    def __init__(self, tab:TAB):
        self.tab = tab

    def close(self):
        self.tab.close()

    def power_up(self):
        self.tab.set_regulator_voltage(*REG_3V3)
        self.tab.set_regulator_voltage(*REG_1V8)

    def power_down(self):
        self.tab.set_regulator_voltage(REG_1V8[0], 0)
        self.tab.set_regulator_voltage(REG_1V8[1], 0)

    def enable(self):
        self.tab.set_pio(PIO_ENABLE,1)

    def disable(self):
        self.tab.set_pio(PIO_ENABLE,0)

    def reset(self):
        self.tab.set_pio(PIO_RESET,0)
        self.tab.set_pio(PIO_RESET,1)
    