
# import with nothing in the __init__.py
from instr.test_adapter.tab_a import TabA

tab = TabA()

tab.open()

tab.power_up()
tab.enable()
tab.reset()
tab.power_down()

tab.close()
