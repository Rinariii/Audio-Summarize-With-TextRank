def mahasiswa_reguler(uts, uas, prak, *aktif):
    rata_aktif = sum(aktif) / len(aktif)
    average = (30/100) * uts + (35/100) * uas + (30/100) * prak + (5/100) * rata_aktif
    return average

def mahasiswa_alihjenis(uts, uas, prak, *aktif, matrikulasi):
    rata_aktif = sum(aktif) / len(aktif)
    average = (25/100) * uts + (25/100) * uas + (20/100) * prak + (5/100) * rata_aktif + (25/100) * matrikulasi
    return average


angka = input()

parts = [p.strip() for p in angka.split(",")]
nilai = []
matrikulasi = None
for p in parts :
    if "matrikulasi" in p.lower():
        matrikulasi = float(p.split("=")[1].strip())
    else:
        nilai.append(float(p))
        
if len(nilai) < 4:
    print("Error input nilai kurang/tidak valid")
    
else :
    uts,uas,prak,*aktif = nilai
    if matrikulasi is None :
        hasil = mahasiswa_reguler(uts,uas,prak,*aktif)
        print(hasil)
    else :
        hasil = mahasiswa_alihjenis(uts,uas,prak,*aktif,matrikulasi=matrikulasi)
        print(hasil)
                