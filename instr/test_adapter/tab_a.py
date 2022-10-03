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

class TabA(TAB):

    def power_up(self):
        self.set_regulator_voltage(REG_ID, REG_VOLT)

    def power_down(self):
        self.set_regulator_voltage(REG_ID, 0)

    def enable(self):
        self.set_pio(PIO_ENABLE,1)

    def disable(self):
        self.set_pio(PIO_ENABLE,0)

    def reset(self):
        self.set_pio(PIO_RESET,0)
        self.set_pio(PIO_RESET,1)
    