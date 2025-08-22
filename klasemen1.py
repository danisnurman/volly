import pandas as pd

# Data hasil rekap
data = {
    "No": [1, 2, 3, 4, 5, 6],
    "Tim": ["RT 01", "RT 02", "RT 03", "RT 04", "RT 05", "RT 06"],
    "Main": [1, 1, 1, 1, 1, 1],
    "Menang": [0, 0, 0, 1, 1, 1],
    "Kalah": [1, 1, 1, 0, 0, 0],
    "Total Skor (+)": [98, 51, 54, 75, 75, 109],
    "Total Skor (-)": [109, 75, 75, 54, 51, 98],
    "Selisih Skor": [-11, -24, -21, 21, 24, 11],
    "Total Set (+)": [2, 0, 0, 3, 3, 3],
    "Total Set (-)": [3, 3, 3, 0, 0, 2]
}

# Buat DataFrame
df = pd.DataFrame(data)

# Urutkan untuk klasemen: berdasarkan Menang, Set Menang, dan Selisih Skor
df_sorted = df.sort_values(by=["Menang", "Total Set (+)", "Selisih Skor"], ascending=[False, False, False])

# Reset indeks biar rapi
df_sorted.reset_index(drop=True, inplace=True)

# Tampilkan klasemen
print(df_sorted)
