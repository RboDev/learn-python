# using a factory function to instanciate the test adapter board
from instr.test_adapter import create

tab = create()

tab.power_up()
tab.enable()
tab.reset()
tab.power_down()

# :-(... wanted to yield the tab to close it automatically in the factory
tab.close()

# When the user knows what he's doing
tab = create(port="COM5", pet="cat")
tab.close()
