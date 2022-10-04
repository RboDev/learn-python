"""Specific high level driver for a DUT of type A.

The Type A DUT:
  - requires a DC Voltage power supply of 3.0V
  - has an ENABLE pin to wake up the chip
  - has a reset pin

"""

from .tab import TAB

REG_ID = 1
REG_VOLT = 3.0

PIO_ENABLE = 1
PIO_RESET = 2

class TabCat:
    """Test Adapter driver for Cat DUT."""
    def __init__(self, tab:TAB):
        self.tab = tab

    def close(self):
        self.tab.close()

    def power_up(self):
        self.tab.set_regulator_voltage(REG_ID, REG_VOLT)

    def power_down(self):
        self.tab.set_regulator_voltage(REG_ID, 0)

    def enable(self):
        self.tab.set_pio(PIO_ENABLE,1)

    def disable(self):
        self.tab.set_pio(PIO_ENABLE,0)

    def reset(self):
        self.tab.set_pio(PIO_RESET,0)
        self.tab.set_pio(PIO_RESET,1)
    