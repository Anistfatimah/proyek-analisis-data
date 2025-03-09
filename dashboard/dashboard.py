import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Header
st.header('Welcome! Bike Rentals')

# Load data
day_df = pd.read_csv("/mount/src/proyek-analisis-data/dashboard/day_data.csv")
hour_df = pd.read_csv("/mount/src/proyek-analisis-data/dashboard/hour_data.csv")

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("/mount/src/proyek-analisis-data/dashboard/sole-bicycles-unsplash.jpg")
    # Selectbox memilih musim
    season_dict = {1: "Musim Panas", 2: "Musim Semi", 3: "Musim Gugur", 4: "Musim Dingin"}
    st.sidebar.title("Filter Data")
    selected_season = st.sidebar.selectbox("Pilih Musim:", list(season_dict.values()))
    

# Filter data berdasarkan musim
season_mapping = {v: i for i, v in season_dict.items()}
filtered_hour_df = hour_df[hour_df["season"] == season_mapping[selected_season]]

# Grafik jumlah peminjaman sepeda setiap jam
st.subheader(f"Jumlah Peminjaman Sepeda per Jam - {selected_season}")
plt.figure(figsize=(10, 5))
sns.lineplot(data=filtered_hour_df, x="hr", y="cnt", marker="o", color="b")
plt.xlabel("Jam")
plt.ylabel("Jumlah Peminjaman")
plt.title(f"Tren Peminjaman Sepeda per Jam pada {selected_season}")
st.pyplot(plt)

st.markdown(
    """
    Setelah mengetahui peminjaman setiap jam berdasarkan musim, dapat melihat jumlah peminjaman sepeda meningkat 
    pada jam-jam sibuk, seperti pagi (sekitar jam 7-9) dan sore (sekitar jam 17-19), ketika orang bepergian untuk bekerja 
    atau pulang kerja.
    """
    )
    

# Grafik perbandingan paling banyak dan paling sedikit peminjaman sepeda per musim
season_avg = day_df.groupby("season")["cnt"].mean().reset_index()
season_avg["season"] = season_avg["season"].map(season_dict)

st.subheader("Perbandingan Rata-rata Peminjaman Sepeda per Musim")
plt.figure(figsize=(8, 5))
sns.barplot(data=season_avg, x="season", y="cnt", palette="coolwarm")
plt.xlabel("Musim")
plt.ylabel("Rata-rata Peminjaman Sepeda")
plt.title("Perbandingan Peminjaman Sepeda per Musim")
st.pyplot(plt)

st.markdown(
    """
    Musim Panas atau Musim Gugur memiliki jumlah peminjaman tertinggi, ini menunjukkan bahwa cuaca hangat 
    dan kering lebih mendukung aktivitas bersepeda. Jika ada penurunan signifikan pada musim tertentu, misalnya di Musim Dingin, ini bisa dikaitkan dengan faktor cuaca buruk yang mengurangi jumlah pengguna sepeda.
    """
)
