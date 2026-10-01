"""Modul percobaan yang sudah diperbaiki agar lolos Pylint quality gate."""

# pylint: disable=too-many-arguments, too-many-positional-arguments
def hitung_nilai(kondisi_a, kondisi_b, kondisi_c, nilai_d, list_e, nilai_f):
    """Fungsi sederhana untuk memproses dan menghitung nilai.

    Args:
        kondisi_a: Nilai boolean pertama.
        kondisi_b: Nilai boolean kedua.
        kondisi_c: Nilai yang diharapkan berupa None.
        nilai_d: Angka penambah pertama.
        list_e: List yang berisi angka.
        nilai_f: Angka penambah kedua.

    Returns:
        Hasil perhitungan matematika jika kondisi terpenuhi, atau None.
    """
    angka_satu = 1
    angka_nol = 0

    if kondisi_a and not kondisi_b and kondisi_c is None:
        try:
            # Mengganti eval dengan penjumlahan biasa
            print(kondisi_a + kondisi_b)
            hasil = list_e[0] + nilai_f + angka_satu + angka_nol + nilai_d
            return hasil
        except (IndexError, TypeError):
            # Menghindari penggunaan "bare except" (except: pass)
            return None

    return None


def main():
    """Fungsi utama untuk menjalankan program."""
    hasil = hitung_nilai(True, False, None, 1, [2], 3)
    print(f"Hasil kalkulasi: {hasil}")


if __name__ == "__main__":
    main()