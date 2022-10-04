"""Helper functions for TAB"""

from logging import warning
from .tab import TAB


def find_tab_port():
    """Find the COM port where the TAB is attached"""
    # TODO: find "TAB" in the list of COM ports
    # see: https://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.list_ports
    return "COM1"


def create(port=None, pet=None):
    """Create the Test Adapter Board for the DUT.

    Args:
        port (str, optional): DUT Type, autodetect if None. Defaults to None.
        pet (str, optional): COM PORT, autodetect if None. Defaults to None.
    """
    if port is None:
        port = find_tab_port()

    tab = TAB()
    tab.open(port=port)

    pet = tab.get_pet()

    if pet.lower() == "dog":
        from .tab_dog import TabDog
        return TabDog(tab)
        
    elif pet.lower() == "cat":
        from .tab_cat import TabCat
        return TabCat(tab)
    else:
        warning(f"{pet} not found, returning generic TAB")
        return tab

    # # Close the TAB after usage
    # tab.close()
