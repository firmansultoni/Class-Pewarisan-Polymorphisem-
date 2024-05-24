class Ikan:
    def __init__(self, jenis, jumlah, bobot):
        self.jenis = jenis
        self.jumlah = jumlah
        self.bobot = bobot

    def kebutuhan_pakan_per_hari(self):
        raise NotImplementedError("Subclass harus mengimplementasikan metode ini")

    def hitung_hari_panen(self):
        raise NotImplementedError("Subclass harus mengimplementasikan metode ini")

    def total_kebutuhan_pakan_hingga_panen(self):
        raise NotImplementedError("Subclass harus mengimplementasikan metode ini")

class Lele(Ikan):
    def __init__(self, jumlah, bobot):
        super().__init__('lele', jumlah, bobot)

    def kebutuhan_pakan_per_hari(self):
        if 1 <= self.bobot <= 10:
            return (0.10 * self.bobot) * self.jumlah
        elif 10 < self.bobot <= 50:
            return (0.08 * self.bobot) * self.jumlah
        elif 50 < self.bobot <= 100:
            return (0.06 * self.bobot) * self.jumlah
        elif 100 < self.bobot <= 200:
            return (0.05 * self.bobot) * self.jumlah
        elif 200 < self.bobot <= 300:
            return (0.04 * self.bobot) * self.jumlah
        elif 300 < self.bobot <= 500:
            return (0.03 * self.bobot) * self.jumlah
        else:
            return 0

    def hitung_hari_panen(self):
        if self.bobot >= 500:
            return 0
        hari = 0
        bobot_sekarang = self.bobot
        while bobot_sekarang < 500:
            hari += 1
            if 1 <= bobot_sekarang <= 10:
                bobot_sekarang += 0.10 * bobot_sekarang
            elif 10 < bobot_sekarang <= 50:
                bobot_sekarang += 0.08 * bobot_sekarang
            elif 50 < bobot_sekarang <= 100:
                bobot_sekarang += 0.06 * bobot_sekarang
            elif 100 < bobot_sekarang <= 200:
                bobot_sekarang += 0.05 * bobot_sekarang
            elif 200 < bobot_sekarang <= 300:
                bobot_sekarang += 0.04 * bobot_sekarang
            elif 300 < bobot_sekarang <= 500:
                bobot_sekarang += 0.03 * bobot_sekarang
        return hari

    def total_kebutuhan_pakan_hingga_panen(self):
        total_pakan = 0
        bobot_sekarang = self.bobot
        while bobot_sekarang < 500:
            if 1 <= bobot_sekarang <= 10:
                pakan_harian = (0.10 * bobot_sekarang) * self.jumlah
                bobot_sekarang += 0.10 * bobot_sekarang
            elif 10 < bobot_sekarang <= 50:
                pakan_harian = (0.08 * bobot_sekarang) * self.jumlah
                bobot_sekarang += 0.08 * bobot_sekarang
            elif 50 < bobot_sekarang <= 100:
                pakan_harian = (0.06 * bobot_sekarang) * self.jumlah
                bobot_sekarang += 0.06 * bobot_sekarang
            elif 100 < bobot_sekarang <= 200:
                pakan_harian = (0.05 * bobot_sekarang) * self.jumlah
                bobot_sekarang += 0.05 * bobot_sekarang
            elif 200 < bobot_sekarang <= 300:
                pakan_harian = (0.04 * bobot_sekarang) * self.jumlah
                bobot_sekarang += 0.04 * bobot_sekarang
            elif 300 < bobot_sekarang <= 500:
                pakan_harian = (0.03 * bobot_sekarang) * self.jumlah
                bobot_sekarang += 0.03 * bobot_sekarang
            total_pakan += pakan_harian
        return total_pakan


class Patin(Ikan):
    def __init__(self, jumlah, bobot):
        super().__init__('patin', jumlah, bobot)

    def kebutuhan_pakan_per_hari(self):
        return (0.07 * self.bobot) * self.jumlah

    def hitung_hari_panen(self):
        hari = 0
        bobot_sekarang = self.bobot
        while bobot_sekarang < 500:
            hari += 1
            bobot_sekarang += 0.07 * bobot_sekarang
        return hari

    def total_kebutuhan_pakan_hingga_panen(self):
        total_pakan = 0
        bobot_sekarang = self.bobot
        while bobot_sekarang < 500:
            pakan_harian = (0.07 * bobot_sekarang) * self.jumlah
            bobot_sekarang += 0.07 * bobot_sekarang
            total_pakan += pakan_harian
        return total_pakan


def angka_ke_teks(angka):
    units = ["", "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan"]
    teens = ["sepuluh", "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas", "enam belas", "tujuh belas", "delapan belas", "sembilan belas"]
    tens = ["", "", "dua puluh", "tiga puluh", "empat puluh", "lima puluh", "enam puluh", "tujuh puluh", "delapan puluh", "sembilan puluh"]
    thousands = ["", "ribu", "juta", "milyar", "trilyun"]

    if angka == 0:
        return "nol"

    words = []
    if angka < 0:
        words.append("minus")
        angka = -angka

    def get_words(n):
        if n == 0:
            return []
        elif n < 10:
            return [units[n]]
        elif n < 20:
            return [teens[n - 10]]
        elif n < 100:
            return [tens[n // 10]] + get_words(n % 10)
        elif n < 1000:
            return [units[n // 100]] + ["ratus"] + get_words(n % 100)
        else:
            for i, v in enumerate(thousands):
                if n < 1000 ** (i + 1):
                    return get_words(n // (1000 ** i)) + [v] + get_words(n % (1000 ** i))

    words.extend(get_words(angka))
    return " ".join(word for word in words if word)



def main():
    jenis_ikan = input("Pilih jenis ikan (lele/patin): ").lower()
    jumlah_ikan = int(input("Masukkan jumlah ikan : "))
    bobot_ikan = int(input("Masukkan bobot ikan hari ini (gram): "))
    stok_pakan = float(input("Masukkan stok pakan pelet (kg): "))
    harga_pakan_per_kg = float(input("Masukkan harga pakan per kg (dalam rupiah): ").replace(".", "").replace(",", "."))

    if jenis_ikan == 'lele':
        ikan = Lele(jumlah_ikan, bobot_ikan)
    elif jenis_ikan == 'patin':
        ikan = Patin(jumlah_ikan, bobot_ikan)
    else:
        print("Jenis ikan tidak dikenal")
        return

    kebutuhan_harian = ikan.kebutuhan_pakan_per_hari() / 1000 
    hari_panen = ikan.hitung_hari_panen()
    total_kebutuhan_pakan = ikan.total_kebutuhan_pakan_hingga_panen() / 1000  
    sisa_pakan = stok_pakan - kebutuhan_harian * hari_panen * jumlah_ikan
    total_biaya_pakan = total_kebutuhan_pakan * harga_pakan_per_kg
    sisa_pakan_hari_ini = stok_pakan - kebutuhan_harian
    

    print("\nDetail Pemeliharaan Ikan")
    print(f"Jenis Ikan: {ikan.jenis.capitalize()}")
    print(f"Jumlah Ikan: {angka_ke_teks(jumlah_ikan)} ekor")
    print(f"Total Berat Ikan Hari ini: {jumlah_ikan * bobot_ikan / 1000} gram")
    print(f"Kebutuhan Pakan / Hari hari ini: {kebutuhan_harian:.2f} kg")
    print(f"Perkiraan Hari Panen sampai 500 gram: {hari_panen} hari")
    print(f"Total Kebutuhan Pakan hingga Panen: {total_kebutuhan_pakan:.2f} kg")
    print(f"Total Biaya Pakan: Rp {total_biaya_pakan:,.2f}")
    print(f"Sisa Pakan Hari ini : {sisa_pakan_hari_ini :} kg")



    

if __name__ == "__main__":
    main()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    