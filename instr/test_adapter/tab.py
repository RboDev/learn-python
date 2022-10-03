"""Test Adapter Board

This module defines the generic functions of the TAB board.

"""

class TAB:

    def open(self, *args, **kwargs):
        ...

    def close(self):
        ...

    def set_regulator_voltage(self, reg_id, volt):
        ...

    def set_pio(self, pio_id, state):
        ...
