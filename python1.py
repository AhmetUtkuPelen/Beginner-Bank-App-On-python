print('AUP banka hoşgeldiniz')
print(' *************** İşlem Menümüz Aşağıdaki Gibidir: 1.Para Çekme İşlemi 2.Para Yatırma İşlemi 3.Bakiye Sorgulama İşlemi 4.Çıkış Yapma İşlemi**************')
bakiye = 100000
while True:
    islem=input('işlem seçiniz')
    
    if islem=="4":
        print('Tekrar Bekleriz')
        break
    elif islem=="3":
        print('Bakiyeniz {} liradır'.format(bakiye))
    elif islem=="2":
        miktar= int(input('Ne kadar yatırmak istersiniz?'))
        bakiye += bakiye
    elif islem=="1":
        miktar=int(input('Ne kadar cekmek istersiniz?'))
        if(bakiye - miktar <0):
            print('Bu Miktarı Cekemezsiniz')
            print('Bakiyeniz {} Liradır'.format(bakiye))
            continue
        bakiye-=miktar
    else:
        print('Lutfen Duzgun Bir İşlem Giriniz')