import re

def clean_rupiah(value):
    value = str(value).strip()

    # kalau ada "k" berarti ribuan
    if re.search(r'[kK]', value):
        num = re.findall(r'\d+\.?\d*', value)
        return float(num[0]) * 1000

    # kalau ada koma sebagai desimal (Eropa)
    if "," in value and "." not in value:
        return float(value.replace(",", "."))

    # kalau format 20.5 (desimal)
    if re.match(r'^\d+\.\d+$', value):
        return float(value)

    # hapus semua selain angka & titik
    cleaned = re.sub(r'[^0-9.]', '', value)

    # kalau ada lebih dari 1 titik → anggap pemisah ribuan
    if cleaned.count('.') > 1:
        cleaned = cleaned.replace('.', '')

    return float(cleaned)
