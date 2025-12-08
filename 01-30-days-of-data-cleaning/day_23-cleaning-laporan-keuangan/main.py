from src.clean_rupiah import clean_rupiah
import pandas as pd

def main():
    data = {
        "tanggal": [
            "2025-01-01", 
            "2025-01-02", 
            "2025-01-03", 
            "2025-01-04", 
            "2025-01-05"
        ],
        "deskripsi": [
            "Penjualan A",
            "Penjualan B",
            "Penjualan C",
            "Penjualan D",
            "Penjualan E"
        ],
        "jumlah": [
            "Rp 10.000",
            "15000",
            "20.5",
            "Rp 50k",
            "30000"
        ]
    }

    df = pd.DataFrame(data)

    print("\n DATA ASLI")
    print(df)

    df["jumlah_bersih"] = df["jumlah"].apply(clean_rupiah)

    print("\n DATA SETELAH DIBERSIHKAN")
    print(df)

    df.to_csv("data/laporan_keuangan_clean.csv", index=False)
    print("\n File disimpan: data/laporan_keuangan_clean.csv")

if __name__ == "__main__":
    main()
