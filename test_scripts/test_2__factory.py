# using a factory function to instanciate the test adapter board
from instr.test_adapter import create

tab = create()

tab.power_up()
tab.enable()
tab.reset()
tab.power_down()

# :-( 
tab.tab.close()
