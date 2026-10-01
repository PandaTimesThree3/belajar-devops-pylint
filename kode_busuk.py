"""Modul perbaikan untuk kode_busuk agar lolos pengujian Pylint."""


def tambah_angka(angka_pertama, angka_kedua):
    """Menambahkan dua angka dan mencetak hasilnya.

    Args:
        angka_pertama: Angka pertama yang akan dijumlahkan.
        angka_kedua: Angka kedua yang akan dijumlahkan.

    Returns:
        Hasil penjumlahan dari kedua angka.
    """
    hasil = angka_pertama + angka_kedua
    print(hasil)
    return hasil


def main():
    """Fungsi utama untuk mengeksekusi program."""
    tambah_angka(1, 2)


if __name__ == "__main__":
    main()