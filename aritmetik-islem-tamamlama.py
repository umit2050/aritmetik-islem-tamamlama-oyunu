# Random modülünü çağırıyoruz.
import random

# Olası sonuçların listesi içinden rastgele rakam seçiliyor.
sonuclar = [1, 4, 5, 6, 7, 8, 9, 14, 15, 16]
sonuc = random.choice(sonuclar)

# İşlem ve açıklamalar. Veri almaya başlıyoruz.
a = input(f"""
1 [ ] 2 [ ] 3 [ ] 4 [ ] = {sonuc}

İşlemi gerçekleştirmek için gerekli operatörleri (+ - * /) girin:

1[ ]: """)

# Aldığımız her veriyi, her seferinde ekranda gösteriyoruz.
print(f"1 [{a}] 2 [ ] 3 [ ] 4 [ ] 5 = {sonuc}")

b = input("2[ ]: ")
print(f"1 [{a}] 2 [{b}] 3 [ ] 4 [ ] 5 = {sonuc}")

c = input("3[ ]: ")
print(f"1 [{a}] 2 [{b}] 3 [{c}] 4 [ ] 5 = {sonuc}")

d = input("3[ ]: ")
print(f"1 [{a}] 2 [{b}] 3 [{c}] 4 [{d}] 5 = {sonuc}")

# Aldığımız string değerlerini aritmetik işleçlere dönüştürüp hesaplıyoruz.
hesapla = eval(f"1 {a} 2 {b} 3 {c} 4 {d} 5")

# İşlem sonucunu kontrol ediyoruz
if hesapla == sonuc:
    print("Tebrikler!")
else:
    print("Hatalı işlem! ", hesapla)
    
