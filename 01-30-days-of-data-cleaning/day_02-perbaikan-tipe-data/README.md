# Day 2 – Perbaikan Tipe Data

Hari ini saya belajar:

1. Mengubah kolom:
   - order_date → datetime
   - total_price → numeric
   - age → numeric
2. Biar dataset siap dibersihkan
3. Menggunakan pandas untuk konversi tipe data
4. Menangani error (misal: missing / format salah → NaN)

File yang dipakai:
- data/mini_dataset.csv
- src/load_data.py
- src/clean_types.py
- main.py

Cara menjalankan:
1. Buka terminal di folder day_02
2. Ketik: python main.py
3. Lihat output tipe data & 5 baris pertama

Yang saya pelajari:
- Data yang salah format otomatis jadi NaN
- Total_price dan age sekarang benar-benar numeric
- order_date sudah datetime → siap dipakai untuk filter & analisis