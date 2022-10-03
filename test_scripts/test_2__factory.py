# using a factory function to instanciate the test adapter board
from instr.test_adapter import create_tab_b

tab = create_tab_b()

tab.open()

tab.power_up()
tab.enable()
tab.reset()
tab.power_down()

tab.close()
