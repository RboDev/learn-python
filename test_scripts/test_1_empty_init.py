
# import with nothing in the __init__.py and no factory
from instr.test_adapter.tab import TAB
from instr.test_adapter.tab_cat import TabCat

tab = TAB()
tab.open()

cat = TabCat(tab)


cat.power_up()
cat.enable()
cat.reset()
cat.power_down()

tab.close()
