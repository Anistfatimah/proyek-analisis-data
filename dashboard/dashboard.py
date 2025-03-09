import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Header
st.header('Welcome! Bike Rentals')

# Load data
day_df = pd.read_csv("/workspaces/proyek-analisis-data/dashboard/day_data.csv")
hour_df = pd.read_csv("/workspaces/proyek-analisis-data/dashboard/hour_data.csv")

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("/workspaces/proyek-analisis-data/dashboard/sole-bicycles-unsplash.jpg")
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
