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

streamlit.title("Turnamen Bola Voli Mejing Kidul")

# Daftar tim
teams = ["RT 01", "RT 02", "RT 03", "RT 04", "RT 05", "RT 06"]

# Inisialisasi klasemen
klasemen_putri = pd.DataFrame({
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

# Klasemen Putri
def update_klasemen_putri(timA, timB, skorA, skorB, setA, setB):
    global klasemen_putri

    # Update jumlah main
    klasemen_putri.loc[klasemen_putri["Tim"] == timA, "Main"] += 1
    klasemen_putri.loc[klasemen_putri["Tim"] == timB, "Main"] += 1

    # Update skor
    klasemen_putri.loc[klasemen_putri["Tim"] == timA, "Skor +"] += skorA
    klasemen_putri.loc[klasemen_putri["Tim"] == timA, "Skor -"] += skorB
    klasemen_putri.loc[klasemen_putri["Tim"] == timB, "Skor +"] += skorB
    klasemen_putri.loc[klasemen_putri["Tim"] == timB, "Skor -"] += skorA

    # Update set
    klasemen_putri.loc[klasemen_putri["Tim"] == timA, "Set +"] += setA
    klasemen_putri.loc[klasemen_putri["Tim"] == timA, "Set -"] += setB
    klasemen_putri.loc[klasemen_putri["Tim"] == timB, "Set +"] += setB
    klasemen_putri.loc[klasemen_putri["Tim"] == timB, "Set -"] += setA

    # Tentukan menang/kalah
    if setA > setB:
        klasemen_putri.loc[klasemen_putri["Tim"] == timA, "Menang"] += 1
        klasemen_putri.loc[klasemen_putri["Tim"] == timB, "Kalah"] += 1
        # Poin
        if setA == 2 and setB <= 1:
            klasemen_putri.loc[klasemen_putri["Tim"] == timA, "Poin"] += 2
        # elif setA == 3 and setB == 2:
        #     klasemen_putri.loc[klasemen_putri["Tim"] == timA, "Poin"] += 2
        #     klasemen_putri.loc[klasemen_putri["Tim"] == timB, "Poin"] += 1
    else:
        klasemen_putri.loc[klasemen_putri["Tim"] == timB, "Menang"] += 1
        klasemen_putri.loc[klasemen_putri["Tim"] == timA, "Kalah"] += 1
        # Poin
        if setB == 2 and setA <= 1:
            klasemen_putri.loc[klasemen_putri["Tim"] == timB, "Poin"] += 2
        # elif setB == 3 and setA == 2:
        #     klasemen_putri.loc[klasemen_putri["Tim"] == timB, "Poin"] += 2
        #     klasemen_putri.loc[klasemen_putri["Tim"] == timA, "Poin"] += 1

# Klasemen Putra
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

# def show_klasemen():
#     global klasemen

#     # Urutkan berdasarkan Poin, Selisih Set, Selisih Skor
#     klasemen["Selisih Set"] = klasemen["Set +"] - klasemen["Set -"]
#     klasemen["Selisih Skor"] = klasemen["Skor +"] - klasemen["Skor -"]
#     df_sorted = klasemen.sort_values(by=["Poin", "Selisih Set", "Selisih Skor"], ascending=[False, False, False]).reset_index(drop=True)

#     # Tambahkan nomor urut
#     df_sorted.index = df_sorted.index + 1
#     df_sorted.rename_axis("No", inplace=True)

#     return df_sorted

# Print Klasemen Putri
def show_klasemen_putri():
    global klasemen_putri

    # Hitung selisih
    klasemen_putri["Selisih Set"] = klasemen_putri["Set +"] - klasemen_putri["Set -"]
    klasemen_putri["Selisih Skor"] = klasemen_putri["Skor +"] - klasemen_putri["Skor -"]

    # Urutkan
    df_sorted = klasemen_putri.sort_values(
        by=["Poin", "Selisih Set", "Selisih Skor"],
        ascending=[False, False, False]
    ).reset_index(drop=True)

    # Tambahkan nomor urut
    df_sorted.index = df_sorted.index + 1
    df_sorted.rename_axis("No", inplace=True)

    # ---------- STYLING ----------
    styled = (
        df_sorted.style
        # Gradient hijau utk Poin (semakin tinggi semakin gelap)
        .background_gradient(cmap="Greens", subset=["Poin"])
        # Gradient biru utk Selisih Set
        .background_gradient(cmap="Blues", subset=["Selisih Set"])
        # Gradient oranye utk Selisih Skor
        .background_gradient(cmap="Oranges", subset=["Selisih Skor"])
        .format({"Selisih Set": "{:+d}", "Selisih Skor": "{:+d}"})
    )

    return styled

# Print Klasemen Putra
def show_klasemen():
    global klasemen

    # Hitung selisih
    klasemen["Selisih Set"] = klasemen["Set +"] - klasemen["Set -"]
    klasemen["Selisih Skor"] = klasemen["Skor +"] - klasemen["Skor -"]

    # Urutkan
    df_sorted = klasemen.sort_values(
        by=["Poin", "Selisih Set", "Selisih Skor"],
        ascending=[False, False, False]
    ).reset_index(drop=True)

    # Tambahkan nomor urut
    df_sorted.index = df_sorted.index + 1
    df_sorted.rename_axis("No", inplace=True)

    # ---------- STYLING ----------
    styled = (
        df_sorted.style
        # Gradient hijau utk Poin (semakin tinggi semakin gelap)
        .background_gradient(cmap="Greens", subset=["Poin"])
        # Gradient biru utk Selisih Set
        .background_gradient(cmap="Blues", subset=["Selisih Set"])
        # Gradient oranye utk Selisih Skor
        .background_gradient(cmap="Oranges", subset=["Selisih Skor"])
        .format({"Selisih Set": "{:+d}", "Selisih Skor": "{:+d}"})
    )

    return styled

# ==========================================
# Input hasil pertandingan (contoh data sesuai tabel Anda)
update_klasemen_putri("RT 02", "RT 04", 13, 50, 0, 2)     #1
update_klasemen_putri("RT 02", "RT 05", 59, 65, 1, 2)     #2
update_klasemen_putri("RT 03", "RT 04", 17, 50, 0, 2)     #3
update_klasemen_putri("RT 01", "RT 05", 50, 29, 2, 0)     #4
update_klasemen_putri("RT 04", "RT 06", 50, 26, 2, 0)     #5
update_klasemen_putri("RT 03", "RT 06", 28, 50, 0, 2)     #6
update_klasemen_putri("RT 01", "RT 04", 20, 50, 0, 2)     #7
update_klasemen_putri("RT 02", "RT 03", 50, 39, 2, 0)     #8
update_klasemen_putri("RT 01", "RT 03", 50, 30, 2, 0)     #9
update_klasemen_putri("RT 02", "RT 06", 18, 50, 0, 2)     #10
update_klasemen_putri("RT 04", "RT 05", 50, 31, 2, 0)     #11
update_klasemen_putri("RT 01", "RT 02", 50, 27, 2, 0)     #12
update_klasemen_putri("RT 03", "RT 05", 45, 51, 0, 2)     #13
update_klasemen_putri("RT 01", "RT 06", 50, 41, 2, 0)     #14

# Input hasil pertandingan (contoh data sesuai tabel Anda)
update_klasemen("RT 02", "RT 05", 51, 75, 0, 3)     #1
update_klasemen("RT 03", "RT 04", 54, 75, 0, 3)     #2
update_klasemen("RT 01", "RT 06", 98, 109, 2, 3)    #3
update_klasemen("RT 02", "RT 04", 47, 75, 0, 3)     #4
update_klasemen("RT 03", "RT 06", 103, 97, 2, 3)    #5
update_klasemen("RT 01", "RT 05", 106, 100, 2, 3)   #6
update_klasemen("RT 02", "RT 03", 88, 80, 3, 1)     #7
update_klasemen("RT 05", "RT 06", 112, 92, 3, 2)    #8
update_klasemen("RT 02", "RT 06", 100, 88, 2, 3)    #9
update_klasemen("RT 04", "RT 05", 97, 67, 3, 1)     #10
update_klasemen("RT 01", "RT 03", 77, 51, 3, 0)     #11
update_klasemen("RT 03", "RT 05", 106, 110, 2, 3)   #12
update_klasemen("RT 04", "RT 06", 100, 82, 3, 2)   #13
update_klasemen("RT 01", "RT 02", 97, 81, 3, 1)   #14

# Tampilkan klasemen putri
streamlit.markdown(":orange-background[**Klasemen Tim Putri**]")
streamlit.dataframe(show_klasemen_putri(), use_container_width=True)
streamlit.markdown("*:green[Last update: 26 Agustus 2025 02:41:15]*")

# new line
streamlit.write("\n\n")
streamlit.divider()
streamlit.write("\n\n")

# Tampilkan klasemen putra
streamlit.markdown(":blue-background[**Klasemen Tim Putra**]")
streamlit.dataframe(show_klasemen(), use_container_width=True)
streamlit.write("*:green[Last update: 25 Agustus 2025 23:48:28]*")
