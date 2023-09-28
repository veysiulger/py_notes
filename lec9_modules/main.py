'''
bir paketin icinde birden fazla modul olabilir.
paket, modulu kapsar.
'''
#tum modulu dahil etme
import test_module
test_module.testFunc()

#modulun bir fonksiyonunu dahil etme
from test_module import testFunc
testFunc()