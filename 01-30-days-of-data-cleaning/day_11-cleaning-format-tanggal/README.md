# Day 11 - Cleaning Format Tanggal 📅

Masalah:
Tanggal bisa banyak format berbeda:
- 2024-01-01
- 01/02/2024
- March 3, 2024
- 2024.04.04
- 5-May-2024

Komputer bingung 🤯

Solusi:
- Pakai pandas.to_datetime
- Standarkan semua ke YYYY-MM-DD

Kenapa penting?
✅ Data siap analisis
✅ Siap dipakai AI & dashboard
❌ Kalau kotor → salah hitung, error

Cara jalan:
python main.py
