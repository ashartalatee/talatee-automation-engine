def inspect_data(df):
    print("\n 5 Baris Pertama:")
    print(df.head())

    print("\n Info Dataset:")
    print(df.info())

    print("\n Statistik Deskriptif:")
    print(df.describe(include="all"))

    print("\n Nama Kolom:")
    print(df.columns)