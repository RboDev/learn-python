"""Test Adapter Board

This module provodes the generic TAB board driver.
"""

class TAB:

    def open(self, port="COM1"):
        ...

    def close(self):
        ...

    def get_pet(self) -> str:
        """Returns the pet species attached to the TAB board."""
        return "dog"

    def set_regulator_voltage(self, reg_id, volt):
        ...

    def set_pio(self, pio_id, state):
        ...
