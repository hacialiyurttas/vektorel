print ("╔════════════════════════════════════════╗")
print ("║      PYTHON ÇALIŞMALARI                ║")
print ("║   1-Hesap makinesi                     ║")
print ("║   2-Oyunlar                            ║")
print ("║   3-Çizimler                           ║")
print ("║   4-Rehber                             ║")
print ("║   5-Müşteri Bilgi                      ║")
print ("║   6-Film Listesi                       ║")
print ("║   7-Dizi Listesi                       ║")
print ("║   8-Envanter Listesi                   ║")
print ("║   9-Kasa Defteri                       ║")
print ("║   10-Stok Giriş-Çıkış Listesi          ║")
print ("║   11-Çıkış                             ║")
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
    print ("Hesap Makinesi seçtiniz")
    import hesap_makine_ana_ekran
if secim == "2" :
    print ("Oyunlar seçtiniz")
    import oyun_ana_ekran
if secim == "3" :
    print ("Çizimler seçtiniz")
    import cizim_ana_ekran
if secim == "4" :
    print ("Rehber seçtiniz")
    import cizim_ana_ekran
if secim == "5" :
    print ("Müşteri Bilgi seçtiniz")
    import musteri_bilgi_ekran
if secim == "6" :
    print ("Film Listesi seçtiniz")
    import film_ana_ekran
if secim == "7" :
    print ("Dizi Listesi seçtiniz")
    import dizi_ana_ekran
if secim == "8" :
    print ("Envanter Listesi seçtiniz")
    import envanter_ana_ekran
if secim == "9" :
    print ("Kasa Defteri seçtiniz")
    import kasa_defteri_ana_ekran
if secim == "10" :
    print ("Stok Giriş Çıkış Listesi seçtiniz")
    import stok_ana_ekran
if secim == "11" :
    print ("Programdan çıkış yapılıyor")
    exit
else : print ("yanlış seçim yaptınız")
