'''
paket icerisinde birden fazla paket olabilir.
paket olusturmak icin, paket kodlarinin oldugu klasorde
__init__.py isimli dosya olusturmaliyiz. py bu dosyayi gorunce
paket olarak yorumlar. Bu dosya olmazsa, py, bunun paket
oldugunu anlamaz.
'''

#pakete erisim
from test_package import test_info
test_info.testInfo()

#alt pakete erisim
from test_package.test2_package import test2_info

test2_info.test2()