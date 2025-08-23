# import pandas as pd

# # Data hasil rekap
# data = {
#     "No": [1, 2, 3, 4, 5, 6],
#     "Tim": ["RT 01", "RT 02", "RT 03", "RT 04", "RT 05", "RT 06"],
#     "Main": [1, 1, 1, 1, 1, 1],
#     "Menang": [0, 0, 0, 1, 1, 1],
#     "Kalah": [1, 1, 1, 0, 0, 0],
#     "Total Skor (+)": [98, 51, 54, 75, 75, 109],
#     "Total Skor (-)": [109, 75, 75, 54, 51, 98],
#     "Selisih Skor": [-11, -24, -21, 21, 24, 11],
#     "Total Set (+)": [2, 0, 0, 3, 3, 3],
#     "Total Set (-)": [3, 3, 3, 0, 0, 2]
# }

# # Buat DataFrame
# df = pd.DataFrame(data)

# # Urutkan untuk klasemen: berdasarkan Menang, Set Menang, dan Selisih Skor
# df_sorted = df.sort_values(by=["Menang", "Total Set (+)", "Selisih Skor"], ascending=[False, False, False])

# # Reset indeks biar rapi
# df_sorted.reset_index(drop=True, inplace=True)

# # Tampilkan klasemen
# print(df_sorted)

import streamlit
import pandas as pd

streamlit.title("Turnamen Bola Voli Antar RT")
streamlit.title("Mejing Kidul 2025")
streamlit.write("Klasemen Tim Putra")

# Daftar tim
teams = ["RT 01", "RT 02", "RT 03", "RT 04", "RT 05", "RT 06"]

# Inisialisasi klasemen
klasemen = pd.DataFrame({
    "Tim": teams,
    "Main": 0,
    "Menang": 0,
    "Kalah": 0,
    "Skor +": 0,
    "Skor -": 0,
    "Set +": 0,
    "Set -": 0,
    "Poin": 0
})

def update_klasemen(timA, timB, skorA, skorB, setA, setB):
    global klasemen

    # Update jumlah main
    klasemen.loc[klasemen["Tim"] == timA, "Main"] += 1
    klasemen.loc[klasemen["Tim"] == timB, "Main"] += 1

    # Update skor
    klasemen.loc[klasemen["Tim"] == timA, "Skor +"] += skorA
    klasemen.loc[klasemen["Tim"] == timA, "Skor -"] += skorB
    klasemen.loc[klasemen["Tim"] == timB, "Skor +"] += skorB
    klasemen.loc[klasemen["Tim"] == timB, "Skor -"] += skorA

    # Update set
    klasemen.loc[klasemen["Tim"] == timA, "Set +"] += setA
    klasemen.loc[klasemen["Tim"] == timA, "Set -"] += setB
    klasemen.loc[klasemen["Tim"] == timB, "Set +"] += setB
    klasemen.loc[klasemen["Tim"] == timB, "Set -"] += setA

    # Tentukan menang/kalah
    if setA > setB:
        klasemen.loc[klasemen["Tim"] == timA, "Menang"] += 1
        klasemen.loc[klasemen["Tim"] == timB, "Kalah"] += 1
        # Poin
        if setA == 3 and setB <= 1:
            klasemen.loc[klasemen["Tim"] == timA, "Poin"] += 3
        elif setA == 3 and setB == 2:
            klasemen.loc[klasemen["Tim"] == timA, "Poin"] += 2
            klasemen.loc[klasemen["Tim"] == timB, "Poin"] += 1
    else:
        klasemen.loc[klasemen["Tim"] == timB, "Menang"] += 1
        klasemen.loc[klasemen["Tim"] == timA, "Kalah"] += 1
        # Poin
        if setB == 3 and setA <= 1:
            klasemen.loc[klasemen["Tim"] == timB, "Poin"] += 3
        elif setB == 3 and setA == 2:
            klasemen.loc[klasemen["Tim"] == timB, "Poin"] += 2
            klasemen.loc[klasemen["Tim"] == timA, "Poin"] += 1

def show_klasemen():
    global klasemen
    klasemen["Selisih Set"] = klasemen["Set +"] - klasemen["Set -"]
    klasemen["Selisih Skor"] = klasemen["Skor +"] - klasemen["Skor -"]
    return klasemen.sort_values(by=["Poin", "Selisih Set", "Selisih Skor"], ascending=[False, False, False]).reset_index(drop=True)

# ==========================================
# Input hasil pertandingan (contoh data sesuai tabel Anda)
update_klasemen("RT 02", "RT 05", 51, 75, 0, 3)
update_klasemen("RT 03", "RT 04", 54, 75, 0, 3)
update_klasemen("RT 01", "RT 06", 98, 109, 2, 3)
update_klasemen("RT 02", "RT 04", 47, 75, 0, 3)
update_klasemen("RT 03", "RT 06", 103, 97, 2, 3)
update_klasemen("RT 01", "RT 05", 106, 100, 2, 3)
update_klasemen("RT 02", "RT 03", 88, 80, 3, 1)
update_klasemen("RT 05", "RT 06", 112, 92, 3, 2)
update_klasemen("RT 02", "RT 06", 100, 88, 2, 3)
update_klasemen("RT 04", "RT 05", 97, 67, 3, 1)
update_klasemen("RT 01", "RT 03", 77, 51, 3, 0)

# Tampilkan klasemen sementara
streamlit.write(show_klasemen())
