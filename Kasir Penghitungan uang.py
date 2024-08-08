def hitung_kembalian(total_belanja, uang_dibayar):
    # Daftar pecahan uang yang tersedia
    pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]

    # Cek jika uang yang dibayar kurang dari total belanja
    if uang_dibayar < total_belanja:
        return False

    # Hitung total kembalian
    kembalian = uang_dibayar - total_belanja

    # Pembulatan kembalian ke bawah Rp.100
    kembalian = (kembalian // 100) * 100

    # Hitung jumlah masing-masing pecahan yang harus diberikan
    pecahan_hasil = {}
    for nilai in pecahan:
        if kembalian >= nilai:
            jumlah_pecahan = kembalian // nilai
            pecahan_hasil[nilai] = jumlah_pecahan
            kembalian %= nilai

    return pecahan_hasil

# Jumlah belanja dan uang 
total_belanja = 1250000
uang_dibayar = 200000

hasil = hitung_kembalian(total_belanja, uang_dibayar)

if hasil:
    print("Detail kembalian:")
    for pecahan, jumlah in hasil.items():
        print(f"Rp. {pecahan}: {jumlah} lembar")
else:
    print("False,Kurang Bayar")
