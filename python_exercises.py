# =============================================================================
# Problem 1
# 1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. 
# Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
# 
# Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır.
# Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).
# Liste şeklinde gösterebiliriz.
# [6,28,469]
# =============================================================================

def MukemmelSayi(sayi):
    toplam=0
    for i in range(1,sayi):
        if(sayi % i == 0):
            toplam+=i            
    if(toplam==sayi):
        return "1"
    else:
        return "0"
        
sayi=1    
m_list=[]
while sayi<1000:
    if(MukemmelSayi(sayi)=="1"):        
        m_list.append(sayi)
    sayi+=1

print(m_list)    

# =============================================================================
# =============================================================================
# Problem 2
# Kullanıcıdan 2 tane sayı alarak bu sayıların en büyük ortak bölenini (EBOB) dönen bir tane fonksiyon yazın.
# 

# 12: 1, 2, 3, 4, 6, 12 
# 24: 1, 2, 3, 4, 6, 8, 12, 24
# EBOB:12

# 8 : 1, 2, 4, 8
# 36: 1, 2, 3, 4, 6, 9, 12, 18, 36
# EBOB:4
# =============================================================================


def Ebob(sayi_1,sayi_2):
    ebob = 1
    i=1
    while(i<=sayi_1 and i<=sayi_2):
        if((sayi_1 % i == 0) and (sayi_2 % i == 0)):
            ebob=i
        i+=1
    return ebob

sayi_1 = int(input("Birinci sayıyı giriniz: "))
sayi_2 = int(input("İkinci sayıyı giriniz: "))


print(Ebob(sayi_1,sayi_2))


# =============================================================================
# =============================================================================
# Problem 3
# Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın.
 
# =============================================================================


def ekok_bulma(sayi_1,sayi_2):
    
    i = 2
    ekok = 1
    while True:
        if ((sayi_1 % i == 0) and (sayi_2 % i == 0)):
            ekok *= i

            sayi_1 //= i
            sayi_2 //= i


        elif ((sayi_1 % i ==  0) and (sayi_2 % i != 0)):
            ekok *= i

            sayi_1 //= i


        elif ((sayi_1 % i != 0) and (sayi_2 % i == 0)):
            ekok *= i

            sayi_2 //= i
        else:
            i += 1
        if ((sayi_1 == 1) and (sayi_2 == 1)):
            break
    return ekok

sayi_1 = int(input("Birinci sayıyı giriniz: "))
sayi_2 = int(input("İkinci sayıyı giriniz: "))

print("Ekok:",ekok_bulma(sayi_1,sayi_2))



# =============================================================================
# =============================================================================
# Problem 4
# Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.
# 
# Örnek: 97 ---------> Doksan Yedi
# =============================================================================


lst_birler = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz","on"]
lst_onlar = ["","on","yirmi","otuz","kırk","elli","altmış","yetmiş","seksen","doksan"]

sayi = int(input("Sayi:"))

if(sayi<100 and sayi>9):
    bsmk_birler = int(sayi%10)
    bsmk_onlar = int(sayi//10)
    print("{} ---------> {}".format(sayi,(lst_onlar[bsmk_onlar]+lst_birler[bsmk_birler])))
    
else:
    print("Lütfen iki basamaklı bir sayı giriniz")


# =============================================================================
# =============================================================================
# Problem 5
# 1'den 100'e kadar olan sayılardan pisagor üçgeni oluşturanları ekrana yazdıran bir fonksiyon yazın.
# (a <= 100,b <= 100)
# 
# =============================================================================

psgr_list=[]

for i in range(1,101):
    for j in range(1,101):
        h=(i**2 + j**2) ** 0.5
        if h in range(1,101):
            psgr_list.append((int(i),int(j),int(h)))

psgr_list.sort()

for k in psgr_list:
    print(k)