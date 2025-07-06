print ("╔════════════════════════════════════════╗")
print ("║      Hesap Makinesi                    ║")
print ("║   1-Çarpma                             ║")
print ("║   2-Toplama                            ║")
print ("║   3-Bölme                              ║")
print ("║   4-Çıkarma                            ║")
print ("║   5-Ana Ekran                          ║")
print ("║   6-Çıkış                              ║")
print ("║                                        ║")
print ("║                                        ║")
print ("║                                        ║")
print ("║                                        ║")
print ("║                                        ║")
print ("║                                        ║")
print ("║                                        ║")
print ("║                                        ║")
print ("║                                        ║")
print ("║                                        ║")
print ("║                                        ║")
print ("║                                        ║")
print ("║                                        ║")
print ("║                                        ║")
print ("║                                        ║")
print ("║                                        ║")
print ("║                                        ║")
print ("║                                        ║")
print ("║                                        ║")
print ("║                                        ║")
print ("║                                        ║")
print ("║                                        ║")
print ("║                                        ║")
print ("║   Seciminiz nedir?                     ║")
print ("║                                        ║")
print ("╚════════════════════════════════════════╝")
secim = input()
print ("seçiminiz:",secim," idi")
if secim == "1" :
    print ("Çarpma işlemi yapılacaktır")
    import carpma
if secim == "2" :
    print ("Toplama işlemi yapılacaktır")
    import toplama
if secim == "3" :
    print ("Bölme işlemi yapılacaktır")
    import bolme
if secim == "4" :
    print ("Çıkarma işlemi yapılacaktır")
    import cikarma
if secim == "5" :
    print ("Ana Ekrana dönülecek")
    import proje_ana_ekran
if secim == "6" :
    print ("Programdan Çıkılacaktır")
    exit
else : print ("yanlış değer girdiniz")
