from logic import *
from utils import *

Knowlegde_Based = FolKB(list(map(expr, [
    'Mahasiswa(Andi)',
    'Mahasiswa(Budi)',
    'MataKuliah(AI)',
    'MataKuliah(DataScience)',
    'MataKuliah(Mathematics)',
    'MataKuliah(IntroProgramming)',
    'MataKuliah(SistemOperasi)',
    'MataKuliah(KomunikasiData)',
    'MataKuliah(OrganisasiArsitekturKomputer)',
    'Jadwal(AI, Senin, Jam9)',
    'Jadwal(DataScience, Senin, Jam9)',
    'Jadwal(SistemOperasi, Selasa, Jam10)',
    'Jadwal(KomunikasiData, Senin, Jam8)',
    'Prasyarat(AI, IntroProgramming)',
    'Prasyarat(AI, Mathematics)',
    'Prasyarat(SistemOperasi, OrganisasiArsitekturKomputer)',
    'Lulus(Andi, IntroProgramming)',
    'Gagal(Andi, Mathematics)',
    'SeringAbsen(Budi, OrganisasiArsitekturKomputer)',
    '(Mahasiswa(s) & MataKuliah(c) & Prasyarat(c, p) & Gagal(s, p)) ==> GabisaDaftar(s, c)',
    '(Mahasiswa(s) & MataKuliah(c1) & MataKuliah(c2) & Jadwal(c1, d, t) & Jadwal(c2, d, t) & InginMatkul(s, c1) & InginMatkul(s, c2)) ==> BertabrakanJadwal(s, c1, c2)',
    '(SeringAbsen(s, c)) ==> Gagal(s, c)',
    '(KehadiranTinngi(s, c)) ==> Eligible(s, c)',
    '(Gagal(s, c)) ==> Mengulang(s, c)',
    '(Lulus(s, c)) ==> Not(Mengulang(s, c))'
])))


def tampilkan_hasil(query, hasil):
    if not hasil:
        print("[]")
    else:
        out = []
        for item in hasil:
            if isinstance(item, dict) and len(item) > 0:
                pasangan = [f"{k}: {v}" for k, v in item.items()]
                out.append("{" + ", ".join(pasangan) + "}")
            else:
                out.append(str(item))
        print("[" + ", ".join(out) + "]")

def interpretasi(kb, query, pesan_ya, pesan_tidak):
    hasil = list(kb.ask_generator(expr(query)))
    tampilkan_hasil(query, hasil)
    if hasil:
        print(f"{pesan_ya}\n")
    else:
        print(f"{pesan_tidak}\n")


Knowlegde_Based.tell(expr('InginMatkul(Andi, AI)'))
Knowlegde_Based.tell(expr('InginMatkul(Andi, DataScience)'))


# Pertanyaan 1
print("1. Apakah Andi dapat mendaftar ke AI?")
interpretasi(
    Knowlegde_Based,
    'GabisaDaftar(Andi, AI)',
    "Andi tidak dapat mendaftar ke AI karena gagal pada prasyarat Mathematics.",
    "Andi dapat mendaftar ke AI karena memenuhi semua prasyarat."
)

# Pertanyaan 2
print("2. Apakah Andi dapat mengambil AI dan DataScience bersamaan?")
interpretasi(
    Knowlegde_Based,
    'BertabrakanJadwal(Andi, AI, DataScience)',
    "Terdapat konflik jadwal antara AI dan DataScience (Senin jam 9).",
    "Tidak ada konflik jadwal antara AI dan DataScience."
)

# Pertanyaan 3
print("3. Apa yang terjadi jika kehadiran Andi di Mathematics < 75%?")
interpretasi(
    Knowlegde_Based,
    'Gagal(Andi, Mathematics)',
    "Jika kehadiran Andi di Mathematics < 75%, maka ia gagal pada mata kuliah tersebut.",
    "Andi tidak gagal dalam Mathematics."
)

# Pertanyaan 4
print("4. Apakah Andi harus mengulang IntroProgramming?")
interpretasi(
    Knowlegde_Based,
    'Mengulang(Andi, IntroProgramming)',
    "Andi harus mengulang IntroProgramming.",
    "Andi tidak perlu mengulang IntroProgramming karena sudah lulus."
)

# Pertanyaan 5
print("5. Andi lulus di mata kuliah apa saja?")
hasil = list(Knowlegde_Based.ask_generator(expr('Lulus(Andi, x)')))
tampilkan_hasil('Lulus(Andi, x)', hasil)
print("Menunjukkan mata kuliah yang berhasil diselesaikan oleh Andi.\n")

# Pertanyaan 6
print("6. Mata kuliah apa saja yang terjadwal di hari Senin jam 9?")
hasil = list(Knowlegde_Based.ask_generator(expr('Jadwal(x, Senin, Jam9)')))
tampilkan_hasil('Jadwal(x, Senin, Jam9)', hasil)
print("Menunjukkan daftar mata kuliah yang dijadwalkan pada Senin jam 9.\n")

# Pertanyaan 7
print("7. Apakah Budi dapat mendaftar ke Sistem Operasi?")
interpretasi(
    Knowlegde_Based,
    'GabisaDaftar(Budi, SistemOperasi)',
    "Budi tidak dapat mendaftar ke Sistem Operasi karena gagal pada prasyarat Organisasi dan Arsitektur Komputer.",
    "Budi dapat mendaftar ke Sistem Operasi karena tidak gagal pada prasyarat."
)

# Pertanyaan 8
print("8. Apakah Budi dapat mendaftar ke Komunikasi Data?")
interpretasi(
    Knowlegde_Based,
    'GabisaDaftar(Budi, KomunikasiData)',
    "Budi tidak dapat mendaftar ke Komunikasi Data.",
    "Budi dapat mendaftar ke Komunikasi Data karena tidak ada prasyarat yang gagal."
)

# Pertanyaan 9
print("9. Apakah Budi harus mengulang Organisasi dan Arsitektur Komputer?")
interpretasi(
    Knowlegde_Based,
    'Mengulang(Budi, OrganisasiArsitekturKomputer)',
    "Budi harus mengulang Organisasi dan Arsitektur Komputer karena kehadiran < 75%.",
    "Budi tidak perlu mengulang Organisasi dan Arsitektur Komputer."
)

