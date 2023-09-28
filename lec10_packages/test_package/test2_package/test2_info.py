def test2InfoDirect():
    print("test2 direct")


def test2InfoImported():
    print("test2 imported")

def test2():
    print("test2")
'''
__name__ degiskeni, modulun hangi yolla cagrildigini
kontrol etmektedir. py calisirken, kodlari calistirmadan
once ozel degiskenleri atar. bu ozel degiskenlerden biri
__name__ dir ve her modulde vardir. __name__ 2 deger alabilir;
dosya dogrudan calistirilirsa __main__ olur. ya da modulun adi olur
'''
if __name__=="__main__":
    test2InfoDirect()
else:
    test2InfoImported()
